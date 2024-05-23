#!/usr/bin/python3
"""a py script for BaseCaching module """


class BaseCaching():
    """
    the BaseCaching class defines
    constants of your caching system
    where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4
    IMPLEMENT = "{} must be implemented in your cache class"

    def __init__(self):
        """the contructor method that Initiliaze """
        self.cache_data = {}

    def print_cache(self):
        """the method that prints the cache """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """the method that adds an item in the cache """
        message = self.IMPLEMENT.format("put")
        raise NotImplementedError(message)

    def get(self, key):
        """the method that gets an item by key """
        message = self.IMPLEMENT.format("get")
        raise NotImplementedError(message)
