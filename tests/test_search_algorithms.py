#!/usr/bin/env python3
import pytest
from server.search_algorithms import *


@pytest.fixture
def sorted_list():
    """Fixture for a common sorted list of strings."""
    return ["apple", "banana", "cherry", "date", "fig", "grape"]


@pytest.fixture
def empty_list():
    """Fixture for an empty list."""
    return []


@pytest.fixture
def unsorted_list():
    """Fixture for an unsorted list."""
    return ["banana", "apple", "grape", "fig", "date", "cherry"]


@pytest.fixture
def single_element_list():
    """Fixture for a single element list."""
    return ["apple"]


@pytest.fixture
def duplicate_element_list():
    """Fixture for a list with duplicate elements."""
    return ["apple", "banana", "banana", "cherry", "date", "date"]


def test_bisect_search_found(sorted_list):
    """Test bisect_search when the element is found."""
    assert bisect_search(sorted_list, "cherry")


def test_bisect_search_not_found(sorted_list):
    """Test bisect_search when the element is not found."""
    assert not bisect_search(sorted_list, "kiwi")


def test_bisect_search_first_element(sorted_list):
    """Test bisect_search when the first element is searched."""
    assert bisect_search(sorted_list, "apple")


def test_bisect_search_last_element(sorted_list):
    """Test bisect_search when the last element is searched."""
    assert bisect_search(sorted_list, "grape")


def test_bisect_search_empty(empty_list):
    """Test bisect_search with an empty list."""
    assert not bisect_search(empty_list, "cherry")


def test_bisect_search_single_element(single_element_list):
    """Test bisect_search with a single element list."""
    assert bisect_search(single_element_list, "apple")
    assert not bisect_search(single_element_list, "banana")


def test_bisect_search_duplicates(duplicate_element_list):
    """Test bisect_search with a list containing duplicates."""
    assert bisect_search(duplicate_element_list, "banana")
    assert bisect_search(duplicate_element_list, "date")


def test_bisect_search_type_error(sorted_list):
    """Test bisect_search with incorrect argument types."""
    with pytest.raises(SearchAlgorithmError):
        bisect_search(123, "cherry")
    with pytest.raises(SearchAlgorithmError):
        bisect_search(sorted_list, 123)


def test_jump_search_found(sorted_list):
    """Test jump_search when the element is found."""
    assert jump_search(sorted_list, "date")


def test_jump_search_not_found(sorted_list):
    """Test jump_search when the element is not found."""
    assert not jump_search(sorted_list, "kiwi")


def test_jump_search_first_element(sorted_list):
    """Test jump_search when the first element is searched."""
    assert jump_search(sorted_list, "apple")


def test_jump_search_last_element(sorted_list):
    """Test jump_search when the last element is searched."""
    assert jump_search(sorted_list, "grape")


def test_jump_search_empty(empty_list):
    """Test jump_search with an empty list."""
    assert not jump_search(empty_list, "cherry")


def test_jump_search_single_element(single_element_list):
    """Test jump_search with a single element list."""
    assert jump_search(single_element_list, "apple")
    assert not jump_search(single_element_list, "banana")


def test_jump_search_duplicates(duplicate_element_list):
    """Test jump_search with a list containing duplicates."""
    assert jump_search(duplicate_element_list, "banana")
    assert jump_search(duplicate_element_list, "date")


def test_jump_search_type_error(sorted_list):
    """Test jump_search with incorrect argument types."""
    with pytest.raises(SearchAlgorithmError):
        jump_search(123, "cherry")
    with pytest.raises(SearchAlgorithmError):
        jump_search(sorted_list, 123)


def test_binary_search_recurse_found(sorted_list):
    """Test binary_search_recurse when the element is found."""
    assert binary_search_recurse(sorted_list, "fig")


def test_binary_search_recurse_not_found(sorted_list):
    """Test binary_search_recurse when the element is not found."""
    assert not binary_search_recurse(sorted_list, "kiwi")


def test_binary_search_recurse_first_element(sorted_list):
    """Test binary_search_recurse when the first element is searched."""
    assert binary_search_recurse(sorted_list, "apple")


def test_binary_search_recurse_last_element(sorted_list):
    """Test binary_search_recurse when the last element is searched."""
    assert binary_search_recurse(sorted_list, "grape")


def test_binary_search_recurse_empty(empty_list):
    """Test binary_search_recurse with an empty list."""
    assert not binary_search_recurse(empty_list, "cherry")


def test_binary_search_recurse_single_element(single_element_list):
    """Test binary_search_recurse with a single element list."""
    assert binary_search_recurse(single_element_list, "apple")
    assert not binary_search_recurse(single_element_list, "banana")


def test_binary_search_recurse_duplicates(duplicate_element_list):
    """Test binary_search_recurse with a list containing duplicates."""
    assert binary_search_recurse(duplicate_element_list, "banana")
    assert binary_search_recurse(duplicate_element_list, "date")


def test_binary_search_recurse_type_error(sorted_list):
    """Test binary_search_recurse with incorrect argument types."""
    with pytest.raises(SearchAlgorithmError):
        binary_search_recurse(123, "cherry")
    with pytest.raises(SearchAlgorithmError):
        binary_search_recurse(sorted_list, 123)


def test_binary_search_iter_found(sorted_list):
    """Test binary_search_iter when the element is found."""
    assert binary_search_iter(sorted_list, "apple")


def test_binary_search_iter_not_found(sorted_list):
    """Test binary_search_iter when the element is not found."""
    assert not binary_search_iter(sorted_list, "kiwi")


def test_binary_search_iter_first_element(sorted_list):
    """Test binary_search_iter when the first element is searched."""
    assert binary_search_iter(sorted_list, "apple")


def test_binary_search_iter_last_element(sorted_list):
    """Test binary_search_iter when the last element is searched."""
    assert binary_search_iter(sorted_list, "grape")


def test_binary_search_iter_empty(empty_list):
    """Test binary_search_iter with an empty list."""
    assert not binary_search_iter(empty_list, "cherry")


def test_binary_search_iter_single_element(single_element_list):
    """Test binary_search_iter with a single element list."""
    assert binary_search_iter(single_element_list, "apple")
    assert not binary_search_iter(single_element_list, "banana")


def test_binary_search_iter_duplicates(duplicate_element_list):
    """Test binary_search_iter with a list containing duplicates."""
    assert binary_search_iter(duplicate_element_list, "banana")
    assert binary_search_iter(duplicate_element_list, "date")


def test_binary_search_iter_type_error(sorted_list):
    """Test binary_search_iter with incorrect argument types."""
    with pytest.raises(SearchAlgorithmError):
        binary_search_iter(123, "cherry")
    with pytest.raises(SearchAlgorithmError):
        binary_search_iter(sorted_list, 123)


def test_python_linear_search_found(sorted_list):
    """Test python_linear_search when the element is found."""
    assert python_linear_search(sorted_list, "grape")


def test_python_linear_search_not_found(sorted_list):
    """Test python_linear_search when the element is not found."""
    assert not python_linear_search(sorted_list, "kiwi")


def test_python_linear_search_first_element(sorted_list):
    """Test python_linear_search when the first element is searched."""
    assert python_linear_search(sorted_list, "apple")


def test_python_linear_search_last_element(sorted_list):
    """Test python_linear_search when the last element is searched."""
    assert python_linear_search(sorted_list, "grape")


def test_python_linear_search_empty(empty_list):
    """Test python_linear_search with an empty list."""
    assert not python_linear_search(empty_list, "cherry")


def test_python_linear_search_single_element(single_element_list):
    """Test python_linear_search with a single element list."""
    assert python_linear_search(single_element_list, "apple")
    assert not python_linear_search(single_element_list, "banana")


def test_python_linear_search_duplicates(duplicate_element_list):
    """Test python_linear_search with a list containing duplicates."""
    assert python_linear_search(duplicate_element_list, "banana")
    assert python_linear_search(duplicate_element_list, "date")


def test_python_linear_search_type_error(sorted_list):
    """Test python_linear_search with incorrect argument types."""
    with pytest.raises(SearchAlgorithmError):
        python_linear_search(123, "cherry")
    with pytest.raises(SearchAlgorithmError):
        python_linear_search(sorted_list, 123)
