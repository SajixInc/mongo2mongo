from pymongo import MongoClient
import pymongo
import urllib.parse

def staggingtoprod(from_database,username1,password1,username2,password2,to_database,ipaddress,ipaddress1):
    try:
        y = []
        mongodb_dbname1 = from_database
        print(from_database,username1,password1,username2,password2,to_database,ipaddress,ipaddress1)
        Username = urllib.parse.quote_plus(username1)
        Username1 = urllib.parse.quote_plus(username2)

        Password = urllib.parse.quote_plus(password1)
        Password1 = urllib.parse.quote_plus(password2)

        myclient1 = MongoClient('mongodb://%s:%s@%s:27017' % (Username, Password, ipaddress))
        mydb1 = myclient1[mongodb_dbname1]
        migration = mydb1.list_collection_names()
        print(myclient1)
        mongodb_dbname2 = to_database
        # username = urllib.parse.quote_plus(Username)
        # password = urllib.parse.quote_plus(Password)
        print('---------- username2',Username1)
        myclient2 = MongoClient('mongodb://%s:%s@%s:27017' % (Username1, Password1, ipaddress1))
        print(myclient2)
        print(myclient2)
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





