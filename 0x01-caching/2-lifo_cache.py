#!/usr/bin/env python3
"""
LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache implements a caching system with a Last-In-First-Out (LIFO)
    eviction policy.
    """

    def __init__(self):
        """
        Initialize the LIFO cache system.
        """
        super().__init__()
        self.last_key = None  # To keep track of the last inserted key

    def put(self, key, item):
        """
        Add an item in the cache.

        If either key or item is None, do nothing.
        If the cache exceeds the MAX_ITEMS limit, discard the last item added
        (LIFO).
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if self.last_key:
                print(f"DISCARD: {self.last_key}")
                del self.cache_data[self.last_key]

        self.cache_data[key] = item
        self.last_key = key  # Update the last inserted key

    def get(self, key):
        """
        Get an item by key from the cache.

        Return None if the key is None or doesn't exist in the cache.
        """
        return self.cache_data.get(key, None)
