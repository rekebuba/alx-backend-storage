#!/usr/bin/env python3
"""
Python function that changes all topics of a school
document based on the name
"""

from typing import List


def update_topics(mongo_collection, name: str, topics: List[str]):
    """changes all topics of a school document based on the name

    Args:
        mongo_collection: pymongo collection object
        name (str): the school name to update
        topics (List):  list of topics approached in the school
    """
    mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})
