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
def sort_method(request):
    sorting_method = request.param
    return sorting_method


@pytest.mark.parametrize("sort_method", [BubbleSort], indirect=True)
@pytest.mark.parametrize("number_series", [10, 100, 1000], indirect=True)
def test_sort(shuffled_series, number_series, sort_method):
    assert len(number_series) == len(shuffled_series)