#!/usr/bin/env python3
"""This module contains various search algorithms"""
import math
from bisect import bisect_left
from typing import List


class SearchAlgorithmError(TypeError):
    """
    Error class raised when error is encountered in the search algorithms.
    """

    pass


# Custom error object for argument type errors
arg_error_obj = SearchAlgorithmError(
    "Argument type to function is wrong, function takes arguments of "
    "type 'List' and 'str' respectively"
)


def bisect_search(sorted_arr: List[str], search_str: str) -> bool:
    """
    Implementation of the binary search algorithm using the bisect_left
    function of python bisect module

    Args:
        sorted_arr (List[str]): The sorted List of strings to search through.
        search_str (str): The string to search for.

    Returns:
        bool: True if the search string is found in the sorted array, False
            otherwise.
    """
    if not isinstance(sorted_arr, list) or not isinstance(search_str, str):
        raise arg_error_obj

    idx: int = bisect_left(sorted_arr, search_str)
    if idx < len(sorted_arr) and sorted_arr[idx] == search_str:
        return True
    else:
        return False


def jump_search(sorted_arr: List[str], search_str: str) -> bool:
    """
    Implementation of the jump search algorithm.

    Args:
        sorted_arr (List[str]): The sorted List of strings to search through.
        search_str (str): The string to search for.

    Returns:
        bool: True if the search string is found in the sorted array, False
            otherwise.
    """
    if not isinstance(sorted_arr, list) or not isinstance(search_str, str):
        raise arg_error_obj

    # check if the last element in the sorted array is less than the
    # search string
    arr_size: int = len(sorted_arr)
    if (not sorted_arr) or (search_str > sorted_arr[-1]):
        return False

    # obtain the block size for each sub-array
    block_size: int = int(math.sqrt(arr_size))

    # iterate over each block in the array
    for min_idx in range(0, arr_size, block_size):
        # obtain the maximum index of a block
        max_idx: int = min_idx + block_size - 1
        # guard against over indexing error
        if max_idx >= arr_size:
            max_idx = arr_size - 1

        # check if the maximum element in the block is less than
        # the search string
        if sorted_arr[max_idx] < search_str:
            continue
        else:
            if search_str in sorted_arr[min_idx : (max_idx + 1)]:
                return True  # search string found in array

    return False  # search string not in array


def binary_search_recurse(sorted_arr: List[str], search_str: str) -> bool:
    """
    Implementation of the binary search algorithm using recursion.

    Args:
        sorted_arr (List[str]): The sorted List of strings to search through.
        search_str (str): The string to search for.

    Returns:
        bool: True if the search string is found in the sorted array, False
            otherwise.
    """
    if not isinstance(sorted_arr, list) or not isinstance(search_str, str):
        raise arg_error_obj

    # check for empty List
    if not sorted_arr:
        return False

    # get the size of the sorted array
    arr_size: int = len(sorted_arr)

    # base condition
    if (sorted_arr) and (arr_size == 1):
        if sorted_arr[0] == search_str:
            return True
        else:
            return False

    # divide the array into 2
    mid_idx: int = arr_size // 2

    # compare the search_string against the maximum of the left array
    if search_str <= sorted_arr[mid_idx - 1]:
        return binary_search_recurse(sorted_arr[:(mid_idx)], search_str)

    # compare the search_string against the maximum of the right array
    elif search_str >= sorted_arr[mid_idx]:
        return binary_search_recurse(sorted_arr[mid_idx:], search_str)
    return False


def binary_search_iter(sorted_arr: List[str], search_str: str) -> bool:
    """
    Implementation of the binary search algorithm using recursion.

    Args:
        sorted_arr (List[str]): The sorted List of strings to search through.
        search_str (str): The string to search for.

    Returns:
        bool: True if the search string is found in the sorted array, False
           otherwise.
    """
    if not isinstance(sorted_arr, list) or not isinstance(search_str, str):
        raise arg_error_obj
    # return false for null array
    if not sorted_arr:
        return False

    while True:
        arr_size: int = len(sorted_arr)  # get the size of the sorted array
        mid_idx: int = arr_size // 2  # get the middle of the array
        if sorted_arr[mid_idx] == search_str:
            return True
        elif arr_size > 1:
            if search_str <= sorted_arr[mid_idx - 1]:
                sorted_arr = sorted_arr[:mid_idx]
            else:
                sorted_arr = sorted_arr[mid_idx:]
        else:
            return False


def python_linear_search(sorted_arr: List[str], search_str: str) -> bool:
    """
    Implementation of python native linear search algorithm
    Args:
        sorted_arr (List[str]): The sorted List of strings to search through.
        search_str (str): The string to search for.

    Returns:
        bool: True if the search string is found in the sorted array, False
           otherwise.
    """
    if not isinstance(sorted_arr, list) or not isinstance(search_str, str):
        raise arg_error_obj
    return search_str in sorted_arr
