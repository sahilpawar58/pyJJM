import pymongo
import json

# Connect to MongoDB
client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.cmcgnwy.mongodb.net/")
db = client["IOT"]
collection = db["maharashtra_villages"]

# Load GeoJSON file
with open('combined_output.geojson') as f:
    data = json.load(f)

# Insert GeoJSON data into MongoDB
collection.insert_many(data['features'])

# Close connection
client.close()
