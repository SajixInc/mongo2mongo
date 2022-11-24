from pymongo import MongoClient
import pymongo
import urllib.parse

y = []
mongodb_dbname2 = "lifeeazydb_prod"
username = urllib.parse.quote_plus('devops_admin')
password = urllib.parse.quote_plus('Devj0019ej')
myclient2 = MongoClient('mongodb://%s:%s@3.108.11.120:27017' % (username, password))
mydb2 = myclient2[mongodb_dbname2]
migration = mydb2.list_collection_names()

# import json
# delete_existing_documents = True
# table_count_e = []
# table_count_s = []


# def migrate_table(db, table_name, mydb):
#     # For example, the $ sign is allowed in MySQL table names but not in MongoDB Collection names
#     mycursor = db.cursor(dictionary=True)
#     mycursor.execute("SELECT * FROM " + table_name + ";")
#     myresult = mycursor.fetchall()
#
#     mycol = mydb[table_name]
#
#     # insert the documents
#     if len(myresult) == 0:
#         mycol = mydb[table_name]
#         mycol.create_index("ID", unique=True)
#         table_count_s.append(table_name)
#         return mycol
#     elif len(myresult) > 0:
#         table_count_s.append(table_name)
#         y = json.loads(json.dumps(myresult, default=str, indent=4, sort_keys=True))
#         # print(type(y))
#         # data = str(myresult)
#         # print(myresult)
#         x = mycol.insert_many(y)
#         return len(x.inserted_ids)
#     else:
#         return 0

mongodb_host = "mongodb://localhost:27017/"
# mongodb_dbname1 = "lifeeazydatabase"
myclient1 = pymongo.MongoClient(mongodb_host)
mydb1 = myclient1[mongodb_dbname2]

# for col in migration:
#     migrate_table(mysqldb, table[0], mydb)

# for coll in mydb.list_collection_names():
#     print(coll)
# mm = myclient2.list_database_names()
for col in migration:

    data = mydb2[col]

    for x in data.find():
        y.append(x)
    if y == []:
        mycol = mydb2[col]
        pass
    else:
        mycol = mydb1[col]
        mycol.insert_many(y)
        y.clear()
