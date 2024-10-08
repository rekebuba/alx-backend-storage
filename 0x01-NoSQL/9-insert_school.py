#!/usr/bin/env python3
"""
Python function that inserts a new document,
in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection based on kwargs

    Args:
        mongo_collection: pymongo collection object
    """
    new_school = mongo_collection.insert_one({**kwargs})
    return new_school.inserted_id
