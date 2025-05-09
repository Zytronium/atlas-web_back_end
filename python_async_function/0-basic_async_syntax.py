#!/usr/bin/env python3
"""
file for task 0
"""
import random
from asyncio import sleep


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds before returning
    that random delay.
    :param max_delay: max delay in seconds before returning
    :return: the randomly picked delay
    """
    delay: float = random.random() * max_delay
    await sleep(delay)
    return delay
