#!/usr/bin/python3
"""This module contains various search algorithms"""
import math
from .search_algorithms import binary_search_iter
from .search_algorithms import binary_search_recurse
from .search_algorithms import bisect_search
from .search_algorithms import jump_search
from .search_algorithms import python_linear_search
from pathlib import Path
from typing import Callable


class Database:
    """
    This class loads the source file and performs searches using different
    search algorithms.

    Attributes:
        reread_on_query (bool): Whether to reload the data from the file on
                              each query.
        __path (Path): The path to the file containing the data.
        sorting_algorithm (Callable[[List[str]], List[str]]): A function to
                              sort the data.
        __data (List[str]): The data loaded from the file, sorted.
    """

    __data: list[str]
    __path: Path

    def __init__(
        self,
        reread_on_query: bool,
        file_path: Path,
        sorting_algorithm: Callable[[list[str]], list[str]],
    ):
        """
        Initializes the Database with the given parameters, reads and sorts
        the data.

        Args:
            reread_on_query (bool): Whether to reload the data from the file on
                                  each query.
            file_path (Path): The path to the file containing the data.
            sorting_algorithm (Callable[[List[str]], List[str]]): A function to
                                  sort the data.
        """
        self.reread_on_query: bool = reread_on_query
        self.__path: Path = file_path
        self.sorting_algorithm: Callable[[list[str]], list[str]] = (
            sorting_algorithm
        )
        self.__data = []
        self.reload()

    def search(
        self,
        search_algo: Callable[[list[str], str], bool] = jump_search,
        search_str: str = "",
    ):
        """
        Search for the existence of a string in the data using a designated
        search algorithm.

        Args:
            search_algo (Callable[[List[str], str], bool]): The search
                                algorithm function to use.
            search_str (str): The string to search for.

        Returns:
            bool: True if the string is found, False otherwise.
        """
        if self.reread_on_query:
            self.reload()  # Reload data if reread_on_query is True

        return search_algo(self.__data, search_str)

    def reload(self) -> None:
        """method to read the file into memory again"""
        if not self.__path.is_file():
            raise FileNotFoundError("Cannot find search file")
        with open(self.__path) as file_obj:
            data = file_obj.readlines()
            self.__data = self.sorting_algorithm(data)  # sort the data
