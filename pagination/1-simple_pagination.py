#!/usr/bin/env python3
"""
Simple pagination
"""
import csv
import math
from typing import List


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a page of the dataset
        :param page: page number to pull from
        :param page_size: number of items per page
        :return: The data from the specified page
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)

        return self.dataset()[start:end]


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
