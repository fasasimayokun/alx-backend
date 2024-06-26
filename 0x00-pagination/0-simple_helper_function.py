#!/usr/bin/env python3
"""a script for a simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    a func that returns a tuple of size two containing a start index
    and an end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters
    """
    begin = (page - 1) * page_size
    end = begin + page_size
    return (begin, end)
