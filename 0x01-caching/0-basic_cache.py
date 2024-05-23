#!/usr/bin/env python3
"""module for Basic dictionary """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    the basicCache class definition
    """
    def __init__(self) -> None:
        super().__init__()

    def put(self, key, item) -> None:
        """
        the set method that set a new item into the cache through @key
        """
        if key is None or item is None:
           return
        self.cache_data.update({key: item})

    def get(self, key):
        """
        the get method that returns the value in self.cache_data linked to key
        """
        return self.cache_data.get(key, None)
