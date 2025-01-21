from abc import ABC, abstractmethod

class SortInterface(ABC):
    '''Interface class to be implemented by various sorting algorithms'''
    @abstractmethod
    def sort(nums: list[int]) -> None:
        '''
        Method that will sort a list of integers
        to be implemented by concrete classes
        '''
        raise NotImplementedError