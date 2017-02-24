# coding=utf-8
import pymongo
import  types
conn =pymongo.MongoClient('localhost',27017)

db = conn.test

#print(db.collection_names())

cu = db.Url


