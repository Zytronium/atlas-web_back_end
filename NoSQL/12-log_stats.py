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
\tmethod GET: {method_get}
\tmethod POST: {method_post}
\tmethod PUT: {method_put}
\tmethod PATCH: {method_patch}
\tmethod DELETE: {method_delete}
{status_check} status check""")
