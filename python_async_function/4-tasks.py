#!/usr/bin/env python3
"""
file for task 4
"""
import typing
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    Calls task_wait_random() n times using a max delay of max_delay
    :param n: Number of times to run task_wait_random()
    :param max_delay: Max delay per calling task_wait_random()
    :return: A list of all the delays used.
    """
    delays: typing.List[float] = []
    for i in range(n):
        delays.append(await task_wait_random(max_delay))

    return sorted(delays)
