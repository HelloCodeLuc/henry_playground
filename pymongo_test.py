import pymongo

# Step 2: Establish a connection to the MongoDB server
#client = pymongo.MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB connection string
client = pymongo.MongoClient("mongodb+srv://kendalljchan88:l7MamoAXo7ycJeNP@cluster0.o6t9xa8.mongodb.net/?retryWrites=true&w=majority")  


# Step 3: Create a new database or use an existing one
db = client["Cluster0"]  # Change "mydatabase" to your desired database name

# Step 4: Create a collection within the database
collection = db["recipes"]  # Change "mycollection" to your desired collection name

# Step 5: Insert data into the collection
data = [
    {"name": "John", "age": 30},
    {"name": "Jane", "age": 25},
    {"name": "Bob", "age": 35},
]

# Insert multiple documents at once
result = collection.insert_many(data)

# Print the IDs of the inserted documents
print("Inserted document IDs:", result.inserted_ids)


# Define the query filter
query = {"name": "Jane"}

# Use the find_one method to retrieve the document matching the query
result = collection.find_one(query)

# Check if a document was found
if result:
    # Access the "age" field from the result
    jane_age = result.get("age")
    print(f"Jane's age is: {jane_age}")
else:
    print("No document found for Jane")


# Close the MongoDB connection when you're done
client.close()
