import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient("mongodb+srv://fatimzahra:anahna1993@cluster0.nnpe6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client