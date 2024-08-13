#!/usr/bin/env python3
"""sorted by average score"""

list_all = __import__('8-all').list_all


def top_students(mongo_collection):
    """function that returns all students sorted by average score

    Args:
        mongo_collection: pymongo collection object
    """
    students = mongo_collection.aggregate(
        [
            {
                '$project': {
                    '_id': 1,
                    'name': 1,
                    'averageScore': {
                        '$avg': {
                            '$avg': '$topics.score',
                        },
                    },
                    'topics': 1,
                },
            },
            {
                '$sort': {'averageScore': -1},
            },
        ]
    )
    return students
