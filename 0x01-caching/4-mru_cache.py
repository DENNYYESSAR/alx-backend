#!/usr/bin/env python3
"""
MRUCache module
"""

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """
    MRUCache implements a caching system with a Most Recently Used (MRU)
    eviction policy.
    """

    def __init__(self):
        """
        Initialize the MRU cache system.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item in the cache.

        If either key or item is None, do nothing.
        If the cache exceeds the MAX_ITEMS limit, discard the most recently
        used item.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key, _ = self.cache_data.popitem(last=True)
            print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """
        Get an item by key from the cache.

        Return None if the key is None or doesn't exist in the cache.
        """
        if key is None or key not in self.cache_data:
            return None

        self.cache_data.move_to_end(key)
        return self.cache_data[key]
