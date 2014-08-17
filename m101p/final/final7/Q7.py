from pymongo import MongoClient
import pymongo
import sys

# connect to the db on standard port
connection = MongoClient()
db = connection.hw7
# get each collections
images = db.images
albums = db.albums

# set the index
try:
    albums.create_index([("images", pymongo.ASCENDING)])
except:
    print "Unexpected error:", sys.exc_info()[0]

# pack ids into a set
id_set = albums.distinct('images')
# check each img id against the set
for img in images.find():
	if img['_id'] not in id_set:
		images.remove({'_id': img['_id']}) 

# sanity check
count_img = images.find().count()
print "%d images left" %(count_img)

kittens_count = images.find({ "tags": "kittens" }).count()
print "Answer: %d" %(kittens_count)
