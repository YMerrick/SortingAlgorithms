from typing import Callable

from .SortInterface import SortInterface


class StrandSort(SortInterface):
    def __merge_lists(list1: list[int], list2: list[int], compare_function: Callable):
        output = []
        while list1 and list2:
            if not compare_function(list1[0], list2[0]):
                output.append(list1.pop(0))
            else:
                output.append(list2.pop(0))
        output.extend(list1)
        output.extend(list2)
        return output


    def __strand_sort(nums: list[int], compare_function: Callable):
        if len(nums) <= 1:
            return nums
        sublist = [nums.pop(0)]
        i = 0
        while i < len(nums):
            if compare_function(nums[i], sublist[-1]):
                sublist.append(nums.pop(i))
            else:
                i += 1

        return StrandSort.__merge_lists(sublist, StrandSort.__strand_sort(nums, compare_function), compare_function)


    def sort(nums: list[int], reverse: bool = False):
        if not reverse:
            compare_function = lambda a, b: a > b
        else:
            compare_function = lambda a, b: a < b
        new_list = StrandSort.__strand_sort(nums, compare_function)
        nums.clear()
        nums.extend(new_list)
