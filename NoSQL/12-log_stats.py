#!/usr/bin/env python3
"""
Provides some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient()
    collection = client["logs"]["nginx"]

    total_logs = collection.count_documents({})
    method_get = collection.count_documents({"method": "GET"})
    method_post = collection.count_documents({"method": "POST"})
    method_put = collection.count_documents({"method": "PUT"})
    method_patch = collection.count_documents({"method": "PATCH"})
    method_delete = collection.count_documents({"method": "DELETE"})
    status_check = collection.count_documents({"method": "GET", "path": "/status"})

    print(f"""{total_logs} logs
Methods:
    method GET: {method_get}
    method POST: {method_post}
    method PUT: {method_put}
    method PATCH: {method_patch}
    method DELETE: {method_delete}
{status_check} status check""")
