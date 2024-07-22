#!/usr/bin/env python3
'''Calculate the start and end index page_size'''

import csv
import math
from typing import List


def index_range(page, page_size):
    """
    Calculate the start and end index for a given page and page_size.

    Args:
    - page (int): The current page number (1-indexed).
    - page_size (int): The number of items per page.

    Returns:
    - tuple: A tuple containing the start index and end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclude header

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a page from the dataset."""
        assert isinstance(page, int) and page > 0,
        assert isinstance(page_size, int) and page_size > 0,
        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        # Return the slice of the dataset
        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]
