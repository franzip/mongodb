
from pymongo import MongoClient
import pymongo
import sys


# connnecto to the db on standard port
connection = MongoClient()
# get the desired collection
collection = connection.students.grades       


def drop_lower_homework():
	# supply query params
	query = {"type": "homework"}

	try:
		# query and sort 
		result = collection.find(query).sort([('student_id', pymongo.ASCENDING),('score',pymongo.ASCENDING)])
	except:
		print "Unexpected error:", sys.exc_info()[0]	

	curr_student = 0

	for document in result:
		# remove the first document you find for each student_id
		if document["student_id"] == curr_student:
			collection.remove(document)
			curr_student += 1
	
	answer = collection.aggregate([{'$group':{'_id':'$student_id', 'average':{'$avg':'$score'}}}, {'$sort':{'average':-1}}, {'$limit':1}])
	print "The answer is ID number: ", answer["result"][0]["_id"]

drop_lower_homework()