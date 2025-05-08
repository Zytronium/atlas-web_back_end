#!/usr/bin/env python3
"""
function for task 8
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns a function (params: x: float) that multiplies the given multiplier
    :param multiplier: the multiplier
    :return:a function that multiplies the given multiplier
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
