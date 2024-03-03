import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.cmcgnwy.mongodb.net/")
db = client["IOT"]
collection = db["country"]

# Fetch all documents from the collection
cursor = collection.find()

# Print each document
for document in cursor:
    print(document['properties']['NAME_1'])

# Close connection
client.close()
