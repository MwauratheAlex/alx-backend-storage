#!/usr/bin/env python3
"""School by topic module"""
from pymongo.collection import Collection


def schools_by_topic(mongo_collection: Collection, topic):
    """returns the list of school having a specific topic"""
    documents = []
    for document in mongo_collection.find({"topics": topic}):
        documents.append(document)
    return documents
