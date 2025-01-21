from .SortInterface import SortInterface

class InsertionSort(SortInterface):
    def sort(nums, reverse = False):
        if not reverse:
            compare_function = lambda a, b: a < b
        else:
            compare_function = lambda a, b: a > b
        for i in range(1, len(nums)):
            j = i
            while compare_function(nums[j], nums [j - 1]) and j != 0:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1
