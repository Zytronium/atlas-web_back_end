#!/usr/bin/env python3
"""
Simple helper function
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Calculates the start index and end index of the data set for a given page
    of the given page size
    :param page: which page of the data set to use
    :param page_size: how many items of data per page
    :return: a tuple of the start index and end index of the data set for the
    given page of the given page size
    """
    return (page_size * (page - 1), page_size * page)
