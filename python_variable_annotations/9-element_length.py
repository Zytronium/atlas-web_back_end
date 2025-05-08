#!/usr/bin/env python3
"""
function for task 9
"""
import typing


def element_length(lst: typing.Iterable[typing.Sequence])\
        -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """
    I don't want to make any more documentation
    :param lst: 1st element
    :return: length of the 1st element
    """
    return [(i, len(i)) for i in lst]
