#!/usr/bin/env python3
"""AN helper function that show the
starting and ending index"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculate the index range"""
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
