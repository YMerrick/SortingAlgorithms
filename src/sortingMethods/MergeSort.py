from .SortInterface import SortInterface


class MergeSort(SortInterface):
    @staticmethod
    def __merge_lists(left: list[int], right: list[int], reverse: bool):
        if not reverse:
            comparison_function = lambda a, b: a < b
        else:
            comparison_function = lambda a, b: a > b
        output = []
        while left and right:
            if comparison_function(left[0], right[0]):
                output.append(left.pop(0))
            else:
                output.append(right.pop(0))
        output.extend(left)
        output.extend(right)
        return output


    @staticmethod
    def __merge_sort(nums: list[int], reverse: bool):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left, right = nums[:mid], nums[mid:]
        left_side = MergeSort.__merge_sort(left, reverse)
        right_side = MergeSort.__merge_sort(right, reverse)
        return MergeSort.__merge_lists(left_side, right_side, reverse)


    @staticmethod
    def sort(nums: list[int], reverse: bool = False):
        if not reverse:
            pass
        sorted_list = MergeSort.__merge_sort(nums, reverse)
        nums.clear()
        nums.extend(sorted_list)
