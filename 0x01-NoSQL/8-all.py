#!/usr/bin/env python3
"""Module contains the function list_all"""


def list_all(mongo_collection):
    """Lists all documents in mongo_collection"""
    documents = []
    for doc in mongo_collection.find():
        documents.append(doc)
    return documents
