#!/usr/bin/env python3
""" MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Least Recently Used eviction policy caching system
    """

    def __init__(self):
        """
        Initialize MRUCache
        """
        super().__init__()
        self.access_order = []

    def put(self, key, item):
        """
        Adds an item in the cache with a key using MRU replacement
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.access_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.access_order.pop()
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        self.cache_data[key] = item
        self.access_order.append(key)

    def get(self, key):
        """
        Gets an item from the cache from a key and mark it as recently used
        """
        if key is not None and key in self.cache_data:
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache_data[key]

        return None
