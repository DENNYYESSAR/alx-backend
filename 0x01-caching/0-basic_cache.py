#!/usr/bin/env python3
"""
BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache is a basic caching system that inherits from BaseCaching.
    This cache has no limit on the number of items.
    """

    def put(self, key, item):
        """
        Add an item in the cache.

        If either key or item is None, do nothing.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key from the cache.

        Return None if the key is None or doesn't exist.
        """
        return self.cache_data.get(key, None)
