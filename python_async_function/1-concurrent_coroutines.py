#!/usr/bin/env python3
"""
file for task 1
"""
import typing
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    Calls wait_random() n times using a max delay of max_delay
    :param n: Number of times to run wait_random()
    :param max_delay: Max delay per calling wait_random()
    :return: A list of all the delays used.
    """
    delays: typing.List[float] = []
    for i in range(n):
        delays.append(await wait_random(max_delay))

    return sorted(delays)
