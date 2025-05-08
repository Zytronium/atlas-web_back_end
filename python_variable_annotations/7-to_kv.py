#!/usr/bin/env python3
"""
function for task 7
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    does a thing
    :param k: a string
    :param v: an integer or a float
    :return: a tuple of the string and the square of the value as a float
    """
    return (k, float(v ** 2))
