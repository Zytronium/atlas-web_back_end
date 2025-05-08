#!/usr/bin/env python3
"""
function for task 6
"""
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """
    I don't want to document these extremely straightforward functions anymore
    :param mxd_lst: list of ints and floats
    :return: sum of the numbers inside the given list
    """
    return float(sum(mxd_lst))
