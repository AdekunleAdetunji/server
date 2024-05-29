#!/usr/bin/env python3
import pytest
from pathlib import Path
from server.database import Database
from server.search_algorithms import *


# Fixtures
@pytest.fixture
def sorted_list(tmp_path):
    """Fixture for a common sorted list of strings."""
    data = ["apple\n", "banana\n", "cherry\n", "date\n", "fig\n", "grape\n"]
    file_path = tmp_path / "sorted_list.txt"
    file_path.write_text("".join(data))
    return file_path


@pytest.fixture
def empty_file(tmp_path):
    """Fixture for an empty file."""
    file_path = tmp_path / "empty.txt"
    file_path.write_text("")
    return file_path


@pytest.fixture
def single_element_file(tmp_path):
    """Fixture for a single element file."""
    file_path = tmp_path / "single_element.txt"
    file_path.write_text("apple\n")
    return file_path


@pytest.fixture
def duplicate_element_file(tmp_path):
    """Fixture for a file with duplicate elements."""
    data = ["apple\n", "banana\n", "banana\n", "cherry\n", "date\n", "date\n"]
    file_path = tmp_path / "duplicate_elements.txt"
    file_path.write_text("".join(data))
    return file_path


# Helper function for sorting
def sort_function(data):
    return sorted([line.strip() for line in data])


# Tests
@pytest.mark.parametrize(
    "search_algo",
    [
        binary_search_iter,
        binary_search_recurse,
        bisect_search,
        jump_search,
        python_linear_search,
    ],
)
def test_search_found(sorted_list, search_algo):
    """Test search when the element is found."""
    db = Database(
        reread_on_query=False,
        file_path=sorted_list,
        sorting_algorithm=sort_function,
    )
    assert db.search(search_algo, "cherry")


@pytest.mark.parametrize(
    "search_algo",
    [
        binary_search_iter,
        binary_search_recurse,
        bisect_search,
        jump_search,
        python_linear_search,
    ],
)
def test_search_not_found(sorted_list, search_algo):
    """Test search when the element is not found."""
    db = Database(
        reread_on_query=False,
        file_path=sorted_list,
        sorting_algorithm=sort_function,
    )
    assert not db.search(search_algo, "kiwi")


@pytest.mark.parametrize(
    "search_algo",
    [
        binary_search_iter,
        binary_search_recurse,
        bisect_search,
        jump_search,
        python_linear_search,
    ],
)
def test_search_first_element(sorted_list, search_algo):
    """Test search for the first element."""
    db = Database(
        reread_on_query=False,
        file_path=sorted_list,
        sorting_algorithm=sort_function,
    )
    assert db.search(search_algo, "apple")


@pytest.mark.parametrize(
    "search_algo",
    [
        binary_search_iter,
        binary_search_recurse,
        bisect_search,
        jump_search,
        python_linear_search,
    ],
)
def test_search_last_element(sorted_list, search_algo):
    """Test search for the last element."""
    db = Database(
        reread_on_query=False,
        file_path=sorted_list,
        sorting_algorithm=sort_function,
    )
    assert db.search(search_algo, "grape")


@pytest.mark.parametrize(
    "search_algo",
    [
        binary_search_iter,
        binary_search_recurse,
        bisect_search,
        jump_search,
        python_linear_search,
    ],
)
def test_search_empty_file(empty_file, search_algo):
    """Test search with an empty file."""
    db = Database(
        reread_on_query=False,
        file_path=empty_file,
        sorting_algorithm=sort_function,
    )
    assert not db.search(search_algo, "cherry")


@pytest.mark.parametrize(
    "search_algo",
    [
        binary_search_iter,
        binary_search_recurse,
        bisect_search,
        jump_search,
        python_linear_search,
    ],
)
def test_search_single_element_file(single_element_file, search_algo):
    """Test search with a single element file."""
    db = Database(
        reread_on_query=False,
        file_path=single_element_file,
        sorting_algorithm=sort_function,
    )
    assert db.search(search_algo, "apple")
    assert not db.search(search_algo, "banana")


@pytest.mark.parametrize(
    "search_algo",
    [
        binary_search_iter,
        binary_search_recurse,
        bisect_search,
        jump_search,
        python_linear_search,
    ],
)
def test_search_duplicates(duplicate_element_file, search_algo):
    """Test search with a file containing duplicates."""
    db = Database(
        reread_on_query=False,
        file_path=duplicate_element_file,
        sorting_algorithm=sort_function,
    )
    assert db.search(search_algo, "banana")
    assert db.search(search_algo, "date")


@pytest.mark.parametrize(
    "sorting_func",
    [
        sort_function,
        lambda x: sorted(
            [line.strip() for line in x]
        ),  # Another sorting algorithm
    ],
)
def test_sorting_algorithms(sorted_list, sorting_func):
    """Test different sorting algorithms."""
    db = Database(
        reread_on_query=False,
        file_path=sorted_list,
        sorting_algorithm=sorting_func,
    )
    assert db.search(binary_search_iter, "apple")
    assert db.search(binary_search_iter, "grape")


def test_reread_on_query(sorted_list):
    """Test reread_on_query functionality."""
    db = Database(
        reread_on_query=True,
        file_path=sorted_list,
        sorting_algorithm=sort_function,
    )
    assert db.search(binary_search_iter, "cherry")

    # Modify the file
    sorted_list.write_text("kiwi\n" + sorted_list.read_text())
    assert db.search(binary_search_iter, "kiwi")


def test_reload_method(sorted_list):
    """Test the reload method."""
    db = Database(
        reread_on_query=False,
        file_path=sorted_list,
        sorting_algorithm=sort_function,
    )
    db.reload()
    assert db.search(binary_search_iter, "cherry")
