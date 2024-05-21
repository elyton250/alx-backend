#!/usr/bin/env python3
"""This paginates a database"""
import csv
from typing import List, Tuple, Optional


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE: str = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        self.__dataset: Optional[List[List[str]]] = None

    def dataset(self) -> List[List[str]]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset: List[List[str]] = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """Returns a tuple of the first and the last index"""
        try:
            assert page > 0
            assert page_size > 0
        except AssertionError as e:
            print('please input a positive integer as page or page_size')
        start_index: int = (page - 1) * page_size
        end_index: int = start_index + page_size
        return (start_index, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> Optional[List[List[str]]]:
        """This paginates the dataset"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        
        if self.__dataset is None:
            print("Dataset is None. Please initialize the dataset.")
            return None
        else:
            total_pages: float = len(self.__dataset) / page_size
            if page > total_pages:
                return []
            else:
                indexes: Tuple[int, int] = self.index_range(page, page_size)
                return self.__dataset[indexes[0]:indexes[1]]
