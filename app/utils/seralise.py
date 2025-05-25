from bson import ObjectId

def serialize_mongo_docs(docs):
    for doc in docs:
        doc["_id"] = str(doc["_id"])
    return docs