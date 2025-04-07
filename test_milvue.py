from pymilvus import connections, utility

# Connect to Milvus
connections.connect("default", host="localhost", port="19530")

# Check server status
print(utility.get_server_version())

# Verify Milvus is working
print("Milvus is working! Collections:", utility.list_collections())





from pymilvus import Collection, FieldSchema, DataType, CollectionSchema

# Define schema
fields = [
    FieldSchema(name="id", dtype=DataType.INT64, is_primary=True),
    FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=128)
]
schema = CollectionSchema(fields, "test_collection")

# Create collection
collection = Collection("test_collection", schema)
print("Collection created:", collection.name)