from .SortInterface import SortInterface

class SelectionSort(SortInterface):
    def sort(nums: list[int], reverse: bool = False):
        if not reverse:
            compare_function = lambda unsorted_subset: min(unsorted_subset)
        else:
            compare_function = lambda unsorted_subset: max(unsorted_subset)
        for i in range(len(nums)):
            unsorted_subset = nums[i:]
            value = compare_function(unsorted_subset)
            index_of_value = unsorted_subset.index(value) + i
            nums[i], nums[index_of_value] = nums[index_of_value], nums[i]
