
from pymongo import MongoClient
import sys


# connnecto to the db on standard port
connection = MongoClient()
# get the desired collection
collection = connection.m101.hw1       


def find():
	query, selector = {},  { "answer": 1, "_id": 0 }

	try:
		# we have only 1 document here, so unload the cursor into a list
		result = collection.find(query, selector)
		# extract the answer field value
		result = result[0].values()[0]

	except:
		print "Unexpected error:", sys.exc_info()[0]	

	print "The answer is: ", result

find()
