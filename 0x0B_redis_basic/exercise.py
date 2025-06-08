#!/usr/bin/env python3
"""
Exercise.py
"""

import uuid
from typing import Union, Callable, Optional
import redis
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts how many times a method is called
    :param method: The method to decorate
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper that counts how many times a method is called
        :param self: The instance
        :param args: Args
        :param kwargs: KW args
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generates a random uuid key and stores the data in redis with that key
        :param data: Data to store
        :return: The random key generated.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, None]:
        """
        Retrieves data from the Redis database
        :param key: The key associated with the data to retrieve
        :param fn: Callback function to convert data back to desired format
        :return: Data retrieved from the database
        """
        value = self._redis.get(key)

        if value is None:
            return None

        return fn(value) if fn else value

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieves data from the Redis database and automatically
        parameterizes Cache.get with the correct conversion function
        for strings.
        :param key: The key associated with the data to retrieve
        :return: Data retrieved from the database
        """
        return self.get(key, fn=lambda d: d.decode("UTF-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieves data from the Redis database and automatically
        parameterizes Cache.get with the correct conversion function
        for integers.
        :param key: The key associated with the data to retrieve
        :return: Data retrieved from the database
        """
        return self.get(key, fn=int)
