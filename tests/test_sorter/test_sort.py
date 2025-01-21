import pytest
import random

from src.sortingMethods.BubbleSort import BubbleSort


@pytest.fixture
def number_series(request):
    n = request.param
    return list(range(n))


@pytest.fixture
def shuffled_series(number_series):
    shuffled_list = number_series.copy()
    random.shuffle(shuffled_list)
    return shuffled_list


@pytest.fixture
def sort_algo(request):
    sorting_method = request.param
    return sorting_method


@pytest.mark.parametrize("sort_algo", [BubbleSort], indirect=True)
@pytest.mark.parametrize("number_series", [10, 100, 1000], indirect=True)
def test_sort(shuffled_series, number_series, sort_algo):
    # Act
    # Perform sort
    sort_algo.sort(shuffled_series)

    assert shuffled_series == number_series