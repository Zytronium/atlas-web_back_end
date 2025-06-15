#!/usr/bin/env python3
"""
Inserts a new doc to a collection based on kwargs
"""

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new doc to a collection based on kwargs
    :param mongo_collection: The mongoDB collection to list from
    :param kwargs: Keyword arguments to pass to mongo_collection
    :return: The new document's id
    """
    return mongo_collection.insert_one(kwargs).inserted_id
