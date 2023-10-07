import pymongo
import sys

# Replace 'YOUR_MONGO_URI' with your actual MongoDB URI
mongo_uri = 'mongodb+srv://root:Vl8vr5Wmq8q3ZzLH@myfirstcluster.shvov.mongodb.net/?retryWrites=true&w=majority'
myDatabase = 'Dash'

try:
  client = pymongo.MongoClient(mongo_uri)
  
# return a friendly error if a URI error is thrown 
except pymongo.errors.ConfigurationError:
  print("An Invalid URI host error was received. Is your Atlas host name correct in your connection string?")
  sys.exit(1)

# use a database named "myDatabase"
mongo = client.Dash

# use a collection named "recipes"
my_collection = mongo["Dash"]
print("Collections in myDatabase:")
print(mongo.list_collection_names())

# print a few documents from dash.recipes

for x in my_collection.find():
    print(x)