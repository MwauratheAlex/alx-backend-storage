#!/usr/bin/env python3
"""School by topic module"""


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic"""
    documents = []
    for document in mongo_collection.find({"topics": topic}):
        documents.append(document)
    return documents
