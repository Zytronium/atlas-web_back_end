#!/usr/bin/env python3
"""
Replaces all topics of the school document that has a certain name with
certain topics.
"""

def update_topics(mongo_collection, name, topics):
    """
    Replaces all topics of the school document that has the given name
    with the given topics.
    :param mongo_collection: The pymongo collection object
    :param name: The name of the school to update
    :param topics: The list of topics to set for the school
    """
    mongo_collection.update_many(
        { 'name': name },
        { "$set": { 'topics': topics } }
    )
