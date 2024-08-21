#!/usr/bin/env python3
"""
MRUCache module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Represents a Most Recently Used (MRU) cache.
    Inherits from the BaseCaching class.
    """
    def __init__(self):
        """
        Initializes the MRUCache instance.
        Calls the parent class (BaseCaching) constructor.
        """
        super().__init__()
        self.mru_order = []

    def put(self, key, item):
        """
        Adds an item to the cache.
        Discards the most recently used item if the cache size exceeds the
        maximum.
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        if key in self.mru_order:
            self.mru_order.remove(key)
        self.mru_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key = self.mru_order.pop(0)
            print(f"DISCARD: {discarded_key}")
            del self.cache_data[discarded_key]

    def get(self, key):
        """
        Retrieves an item from the cache.
        """
        if key is None or key not in self.cache_data:
            return None

        self.mru_order.remove(key)
        self.mru_order.append(key)
        return self.cache_data[key]
