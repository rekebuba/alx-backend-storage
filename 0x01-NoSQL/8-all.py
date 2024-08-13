#!/usr/bin/env python3
"""a Python function that lists all documents in a collection"""


def list_all(mongo_collection):
    """lists all documents in a collection:

    Args:
        mongo_collection: pymongo collection object
    """
    result = []
    for document in mongo_collection.find():
        result.append(document)
    return result
