import pytest
import random

from src.sortingMethods import (BubbleSort, InsertionSort, SortInterface,
                                SelectionSort,)

sort_algo_list = [
    BubbleSort,
    InsertionSort,
]
pytestmark = pytest.mark.parametrize("sort_algo", sort_algo_list, indirect=True)

size_of_n = [
    10,
    100,
    1000,
]


@pytest.fixture
def number_series(request):
    n = request.param
    return list(range(n))


@pytest.fixture
def all5(request):
    n = request.param
    return [5] * n


@pytest.fixture
def sort_algo(request):
    sorting_method = request.param
    return sorting_method


@pytest.mark.parametrize("number_series", size_of_n, indirect=True)
def test_sort_with_series(number_series: list[int], sort_algo: SortInterface):
    # Act
    test_space = number_series.copy()
    random.shuffle(test_space)
    # Perform sort
    sort_algo.sort(test_space)

    assert test_space == number_series


@pytest.mark.parametrize("all5", size_of_n, indirect=True)
def test_sort_with_all_fives(all5: list[int], sort_algo: SortInterface):
    test_space = all5.copy()
    sort_algo.sort(test_space)
    assert test_space == all5


@pytest.mark.parametrize("number_series", size_of_n, indirect=True)
def test_sort_with_reversed(number_series: list[int], sort_algo: SortInterface):
    test_space = number_series.copy()
    test_space.reverse()
    sort_algo.sort(test_space)
    assert test_space == number_series
