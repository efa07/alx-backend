#!/usr/bin/env python3
'''Calculate the start and end index page_size'''

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
