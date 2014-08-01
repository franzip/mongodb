
from pymongo import MongoClient
import sys


# connnecto to the db on standard port
connection = MongoClient()
# select collection
collection = connection.m101.funnynumbers        


magic = 0

try:
    iter = collection.find()
    for item in iter:
        if ((item['value'] % 3) == 0):
            magic = magic + item['value']

except:
    print "Error trying to read collection:" + sys.exc_info()[0]


print "The answer to Homework One, Problem 2 is " + str(int(magic))


