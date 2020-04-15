# Leet code 30-day challenge

# Move Zeroes

"""Given an array nums, write a function to move all 0's to the end of it while 
maintaining the relative order of the non-zero elements.

    >>> move_zeroes([0,1,0,3,12])
    [1,3,12,0,0]


"""

def move_zeroes(nums):
    """Given an array nums, write a function to move all 0's to the end of it while 
    maintaining the relative order of the non-zero elements."""

    # pesudocode:
    # check if the the value is a zero
    # if it is move to end of array
    # move by list slicing? -- 
    # else continue

    for idx, val in enumerate(nums):
        if val == 0:
            idx = nums[-1]
            
    return nums


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** Test Pass! \n")

