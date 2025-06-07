#!/usr/bin/env python3
"""
Exercise.py
"""

import uuid
from typing import Union
from redis import Redis


class Cache:
    def __init__(self):
        self._redis = Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generates a random uuid key and stores the data in redis with that key
        :param data: Data to store
        :return: The random key generated.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
