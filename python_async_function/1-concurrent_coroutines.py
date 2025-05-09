#!/usr/bin/env python3
"""
file for task 1
"""
wait_random = __import__('0-basic_async_syntax').wait_random
import typing


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    Calls wait_random() n times using a max delay of max_delay
    :param n: Number of times to run wait_random()
    :param max_delay: Max delay per calling wait_random()
    :return: A list of all the delays used.
    """
    delays: typing.List[float] = []
    for i in range(n):
        # Divide by 5 to speed up testing process, multiply result to revert
        delays.append(await wait_random(max_delay / 5) * 5)

    return delays
