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


def call_history(method: Callable) -> Callable:
    """
    Decorator that stores the history of inputs and outputs
    for a certain function
    :param method: The method to decorate
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper that stores a function's inputs and outputs history
        in lists in the Redis DB.
        :param self: The instance
        :param args: Args
        :param kwargs: KW args
        """
        key = method.__qualname__
        input_key = f"{key}:inputs"
        output_key = f"{key}:outputs"
        output = method(self, *args, **kwargs)

        self._redis.rpush(input_key, str(args))
        self._redis.rpush(output_key, str(output))
        return output
    return wrapper


def replay(method: Callable):
    """
    Display the count and history of calls to a given
    function. Displays number of calls, which inputs were
    used, and which outputs were returned.
    :param method: The method to replay history for
    """
    rds = method.__self__._redis
    qualname = method.__qualname__

    inputs_key = f"{qualname}:inputs"
    outputs_key = f"{qualname}:outputs"

    inputs = rds.lrange(inputs_key, 0, -1)
    outputs = rds.lrange(outputs_key, 0, -1)

    print(f"{qualname} was called {len(inputs)} times:")
    for inp, outp in zip(inputs, outputs):
        print(f"{qualname}(*{inp.decode()}) -> {outp.decode()}")


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
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
