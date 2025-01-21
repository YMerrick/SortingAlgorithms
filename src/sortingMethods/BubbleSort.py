from .SortInterface import SortInterface

class BubbleSort(SortInterface):
    def sort(nums, reverse = None):
        if not reverse:
            compare_function = lambda a, b: a > b
        else:
            compare_function = lambda a, b: a < b
        for n in range(len(nums), -1, -1):
            for i in range(1, n):
                if compare_function(nums[i - 1], nums[i]):
                    nums[i - 1], nums[i] = nums[i], nums[i - 1]
        return None
