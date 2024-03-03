import pymongo
import time
import random

# MongoDB connection settings
client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.cmcgnwy.mongodb.net/")
db = client["IOT"]
collection = db["flowmeter"]

# Function to insert data into MongoDB
def insert_data(data):
    try:
        collection.insert_one(data)
        print("Data inserted successfully")
    except Exception as e:
        print(f"Error: {e}")

# Main loop to add data at intervals
while True:
    data_to_insert = {"Timestamp": time.time(), "Readings": random.randint(0, 14)}  # Replace with your data
    insert_data(data_to_insert)
    time.sleep(10)  # Insert data every 60 seconds (adjust as needed)
