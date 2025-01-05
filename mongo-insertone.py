import pymongo

myclient = pymongo.MongoClient("mongodb://root:mongo123@mongodb:27017")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydict = { "name": "Aman", "address": "Bangalore" }

x = mycol.insert_one(mydict)