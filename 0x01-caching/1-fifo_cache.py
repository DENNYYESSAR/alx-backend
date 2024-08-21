#!/usr/bin/env python3
"""
FIFOCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache implements a caching system with a First-In-First-Out (FIFO)
    eviction policy.
    """

    def __init__(self):
        """
        Initialize the FIFO cache system.
        """
        super().__init__()
        self.order = []  # To track the order of keys for FIFO

    def put(self, key, item):
        """
        Add an item in the cache.

        If either key or item is None, do nothing.
        If the cache exceeds the MAX_ITEMS limit, discard the first item added
        (FIFO).
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            oldest_key = self.order.pop(0)  # Remove the oldest item
            del self.cache_data[oldest_key]  # Remove from cache
            print(f"DISCARD: {oldest_key}")  # Print the discarded key

        self.cache_data[key] = item
        self.order.append(key)  # Add the key to the end of the order list

    def get(self, key):
        """
        Get an item by key from the cache.

        Return None if the key is None or doesn't exist in the cache.
        """
        return self.cache_data.get(key, None)
