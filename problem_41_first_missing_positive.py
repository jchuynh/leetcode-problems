"""Given an unsorted integer array, find the smallest missing positive integer.
    >>> firstMissingPositive([1, 2, 0])
    3

    >>> firstMissingPositive([3, 4, -1, 1])
    2

    >>> firstMissingPositive([7, 8, 9, 11, 12])
    1
"""

# Your algorithm should run in O(n) time

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """Given an unsorted integer array, find the smallest missing positive integer."""

        # pseudocode
        # sort list?
        # check if for integers are greater than 0
        # find smallest positive integers

        sett_nums = set(nums) # using set is a quicker look-up 
        result = 1 # start with the first positive integer, we do not need to worry about negatives
        while result in sett_nums: # while the integer is in the list
            result +=1 # add 1 until the final integer is not in the list
        return result # return that integer



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** Passed!\n")