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