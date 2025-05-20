#!/usr/bin/env python3
""" FIFOCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    First-in First-out caching system
    """

    def __init__(self):
        """
        Initialize FIFOCache
        """
        super().__init__()
        self.order = []


    def put(self, key, item):
        """
        Adds an item in the cache with a key
        """
        if key is None or item is None:
            return

        if (key not in self.cache_data
                and len(self.cache_data) >= BaseCaching.MAX_ITEMS):
            oldest_key = self.order.pop(0)
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")

        if key not in self.order:
            self.order.append(key)

        self.cache_data[key] = item

    def get(self, key):
        """
        Gets an item from the cache from a key
        """
        if key is not None:
            return self.cache_data.get(key, None)

        return None
