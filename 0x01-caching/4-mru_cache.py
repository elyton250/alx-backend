#!/usr/bin/env python3
"""This is a new caching system"""
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """This is the caching system"""
    def __init__(self):
        """This initializes the class"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """This is the put method"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded_key = self.cache_data.popitem(last=True)[0]
                print(f'DISCARD: {discarded_key}')

    def get(self, key):
        """This gets the key"""
        if key is not None and key in self.cache_data:
            value = self.cache_data.pop(key)
            self.cache_data[key] = value
            return value
        return None
