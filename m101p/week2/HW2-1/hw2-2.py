
from pymongo import MongoClient
import pymongo
import sys


# connnecto to the db on standard port
connection = MongoClient()
# get the desired collection
collection = connection.students.grades       


def find():
	query, selector = {"score": {"$gte": 65}},  { "student_id": 1, "_id": 0 }

	try:
		result = collection.find(query, selector).limit(1).sort("score", pymongo.ASCENDING)
	except:
		print "Unexpected error:", sys.exc_info()[0]	

	print "The answer is id number: ", result[0].values()[0]

find()