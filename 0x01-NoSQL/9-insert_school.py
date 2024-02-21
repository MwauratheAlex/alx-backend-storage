#!/usr/bin/env python3
"""Module contains the function insert_school(mongo_collection, **kwargs)"""


def insert_school(mongo_collection, **kwargs):
    """Inserts new document into collection based on kwargs"""
    inserted_doc = mongo_collection.insert_one(kwargs)
    return inserted_doc.inserted_id
