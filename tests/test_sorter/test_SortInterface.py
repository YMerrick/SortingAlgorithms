import pytest

from src.sortingMethods import SortInterface

def test_SortInterface_sort_method_raises_error():
    with pytest.raises(NotImplementedError):
        SortInterface.sort([])