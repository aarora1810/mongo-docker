import pymongo
myclient = pymongo.MongoClient("mongodb://root:mongo123@mongodb:27017")
mydb = myclient["mydatabase"]
mycol = mydb ["customers"]

x = mycol.find_one()

print(x)