#!/usr/bin/env python3
"""
file for task 0
"""
import asyncio
import random
import typing
from _typeshed import NoneType


async def async_generator() -> typing.Generator[float, NoneType, NoneType]:
    """
    Generator that waits 1 second before yielding a random
    float between 0 and 10, 10 times
    :return: a random number between 0 and 10 (10 times)
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
