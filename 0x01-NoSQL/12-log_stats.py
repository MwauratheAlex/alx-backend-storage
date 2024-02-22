#!/usr/bin/env python3
"""Module contains a Python script that
provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_log_collection = client.logs.nginx

    no_of_logs = nginx_log_collection.count_documents({})
    method_count = {
        'GET': nginx_log_collection.count_documents({'method': 'GET'}),
        'POST': nginx_log_collection.count_documents({'method': 'POST'}),
        'PUT': nginx_log_collection.count_documents({'method': 'PUT'}),
        'PATCH': nginx_log_collection.count_documents({'method': 'PATCH'}),
        'DELETE': nginx_log_collection.count_documents({'method': 'DELETE'}),
    }
    status_check_count = nginx_log_collection.count_documents({
        'method': 'GET',
        'path': '/status'
    })

    print(f"{no_of_logs} logs")
    print("Methods:")
    for method in method_count:
        print(f"\t{method}: {method_count[method]}")
    print(f"{status_check_count} status check")
