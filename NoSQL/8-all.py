#!/usr/bin/env python3
"""
Lists all docs in a MongoDB collection
"""

def list_all(mongo_collection):
    """
    Lists all docs in a collection
    :param mongo_collection: The mongoDB collection to list from
    :return: List of docs, or empty list if there are none.
    """
    return list(mongo_collection.find())
