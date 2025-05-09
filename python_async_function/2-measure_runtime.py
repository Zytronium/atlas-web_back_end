#!/usr/bin/env python3
"""
file for task 2
"""
import time
wait_n = __import__('1-concurrent_coroutines').wait_n



async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for running wait_n(n, max_delay)
    :param n: the max number of times wait_n will run wait_random
    :param max_delay: max delay in seconds to feed into wait_n()
    :return: average time for each time wait_random runs
    """
    start: float = time.time()
    await wait_n(n, max_delay)
    total_time: float = time.time() - start
    return total_time / n
