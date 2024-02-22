#!/usr/bin/env python3
"""Top student module"""
from pymongo.collection import Collection


def top_students(mongo_collection: Collection):
    """returns all students sorted by average score"""
    pipeline = [
        {'$unwind': '$topics'},
        {
            '$group': {
                '_id': '$_id',
                'name': {'$first': '$name'},
                'topics': {'$push': '$topics'},
                'averageScore': {'$avg': '$topics.score'}
            }
        },
        {'$sort': {'averageScore': -1}},
    ]
    students = list(mongo_collection.aggregate(pipeline))
    return students
