#!/usr/bin/env python3
"""a py script for FIFO caching """
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """
    the FIFOCache class definition
    """
    def __init__(self) -> None:
        super().__init__()

    def put(self, key, item) -> None:
        """
        the method used to Assign to the dictionary self.cache_data,
        the item value for the key
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = list(self.cache_data)[0]
            del self.cache_data[first_key]
            print("DISCARD: {}".format(first_key))
        self.cache_data.update({key: item})

    def get(self, key):
        """
        the get method that return the value in self.cache_data linked to key
        """
        return self.cache_data.get(key, None)
