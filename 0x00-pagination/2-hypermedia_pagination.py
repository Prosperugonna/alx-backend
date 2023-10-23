#!/usr/bin/env python3
"""Create a simple pagination"""


import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculate the index range"""
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''Get page method
        '''
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        result = self.dataset()
        try:
            idx = index_range(page, page_size)
            return result[idx[0]: idx[1]]
        except BaseException:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        '''Get hyper pagination'''
        data_len = len(self.dataset())
        data = self.get_page(page, page_size)
        result = {
            "page": page,
            "page_size": page_size if page_size <= len(data) else len(data),
            "total_pages": data_len,
            "data": data,
            "prev_page": page - 1 if page > 1 else None,
            "next_page": page + 1 if page + 1 <= data_len else None
        }
        return result
