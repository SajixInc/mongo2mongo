from pymongo import MongoClient
import pymongo
import urllib.parse
# Local to Server
def localtostagging(from_database,Username,Password,to_database,to_host,ipaddress):
    try:
        y = []
        mongodb_dbname1 = from_database
        mongodb_host = to_host
        myclient1 = pymongo.MongoClient(mongodb_host)
        mydb1 = myclient1[mongodb_dbname1]
        migration = mydb1.list_collection_names()
        print(myclient1)
        mongodb_dbname2 = to_database
        username = urllib.parse.quote_plus(Username)
        password = urllib.parse.quote_plus(Password)
        myclient2 = MongoClient('mongodb://%s:%s@%s:27017' % (username, password, ipaddress))
        mydb2 = myclient2[mongodb_dbname2]
        # migration = mydb2.list_collection_names()

        for col in migration:

            data = mydb1[col]

            for x in data.find():
                y.append(x)
            if y == []:
                mycol = mydb1[col]
                pass
            else:
                mycol = mydb2[col]
                mycol.insert_many(y)
                y.clear()
    except pymongo.errors.BulkWriteError as e:
        print('Database is existing with is name')
    except pymongo.errors.OperationFailure as e:
        print('Check the credentials of Mongodb')
    except ValueError as e:
        print('Check the Local host of Mongodb')