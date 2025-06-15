#!/usr/bin/env python3
"""
Gets a list of the schools that have a specific topic
"""

def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools that have a specific topic
    :param mongo_collection: The pymongo collection object
    :param topic: The topic to search for
    :return: A list of the schools that have the give topic
    """
    return list(mongo_collection.find({"topics": topic}))
