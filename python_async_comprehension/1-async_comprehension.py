#!/usr/bin/env python3
"""
file for task 1
"""
import typing
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """
    Collects 10 random numbers using an async comprehension over
    async_generator, then returns them as a list.
    :return: list of values
    """
    return [value async for value in async_generator()]
