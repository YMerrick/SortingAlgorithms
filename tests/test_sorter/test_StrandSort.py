from src.sortingMethods.StrandSort import StrandSort


def test_merge_lists_with_all_empty():
    list1 = []
    list2 = []
    expected = []
    result = StrandSort._StrandSort__merge_lists(list1,
                                                 list2,
                                                 lambda a, b: a < b)
    assert result == expected


def test_merge_lists_normal_case():
    list1 = [1, 3, 4]
    list2 = [2, 5, 6]
    expected = [1, 2, 3, 4, 5, 6]
    result = StrandSort._StrandSort__merge_lists(list1,
                                                 list2,
                                                 lambda a, b: a > b)
    assert result == expected


def test_merge_lists_with_one_filled():
    list1 = [1, 2, 3]
    list2 = []
    expected = [1, 2, 3]
    result = StrandSort._StrandSort__merge_lists(list1,
                                                 list2,
                                                 lambda a, b: a > b)
    assert result == expected
