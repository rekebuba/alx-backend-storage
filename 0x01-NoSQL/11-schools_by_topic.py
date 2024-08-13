#!/usr/bin/env python3
""" Python function that returns the list of school,
having a specific topic"""


def schools_by_topic(mongo_collection, topic: str):
    """list of school having a specific topic

    Args:
        mongo_collection: pymongo collection object
        topic (str): will be topic searched
    """
    return [result for result in mongo_collection.find({'topics': topic})]
