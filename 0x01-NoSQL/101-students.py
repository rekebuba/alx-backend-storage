#!/usr/bin/env python3
"""sorted by average score"""
list_all = __import__('8-all').list_all

def top_students(mongo_collection):
    """function that returns all students sorted by average score

    Args:
        mongo_collection: pymongo collection object
    """
    students = list_all(mongo_collection)

    for student in students:
        scores = [topic.get('score') for topic in student.get('topics')]
        averageScore = sum(scores) / len(scores)
        mongo_collection.update_one({'_id': student.get('_id')}, {'$set': { 'averageScore' : averageScore}})

    return [result for result in mongo_collection.find().sort({ 'averageScore': -1 })]
