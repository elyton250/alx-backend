#!/usr/bin/env python3
"""this is for base caching system"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """this is a caching system"""
    def __init__(self):
        """initi function"""
        super().__init__()

    def put(self, key, item):
        """this adds into the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """this gets the key"""
        return self.cache_data.get(key, None)
