
from pymongo import MongoClient
import pymongo
import sys


# connnecto to the db on standard port
connection = MongoClient()
# get the desired collection
collection = connection.school.students       


def drop_lower_homework():

	try:
		# no need to sort
		result = collection.find().sort('_id', pymongo.ASCENDING)
	except:
		print "Unexpected error:", sys.exc_info()[0]	

	for document in result:
		# save curr id and doc scores array
		curr_id = document['_id']
		curr_scores = document['scores']
		# pack homework scores into an array for each doc
		scores = [x['score'] for x in document['scores'] if x['type'] == 'homework']
		scores.sort()
		# drop lowest
		curr_scores.remove({'type': 'homework', 'score': scores[0]})
		# now update DB
		collection.update({'_id' : curr_id}, { '$set' : { 'scores' : curr_scores}})
	
	answer = collection.aggregate([{ '$unwind' : '$scores' } , { '$group' : { '_id' : '$_id' , 'average' : { '$avg' : '$scores.score' } } } , { '$sort' : { 'average' : -1 } } , { '$limit' : 1 }])
	print "The answer is the id: ", answer['result'][0]['_id']

drop_lower_homework()