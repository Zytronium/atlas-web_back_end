#!/usr/bin/env python3
"""
file for task 3
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes a max delay and returns an wait_random(max_delay) as an asyncio.Task
    :param max_delay: the max delay to feed to wait_random
    :return: wait_random(max_delay) as an asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
