# Given an array of integers A sorted in non-decreasing order, return an array 
# of the squares of each number, also in sorted non-decreasing order.



class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        """
        >>> sortedSquares([-4,-1,0,3,10])
        [0,1,9,16,100]

        >>> sortedSquares([-7,-3,2,3,11])
        [4,9,9,49.121]

        """
        # NOTES:




        # pseudocode:
        # brute force:
        # for number in A:
        # sq_lst = []
        # for val in A:
            # sq_lst.append(val**2)
        # number**2
        # append to new list
        # print(sq_lst)
        # return sorted(sq_lst)
    

        # try 2
        # for val in A:
        # return sorted(val*val for val in A)


        # two pointer method?:

        # Take a look at the input. The array is sorted so the ends will be
        # a higher value than the middle.
        # So use the pointers at each end to collect the larger values.
        # set pointers
        left = 0 
        right = len(A) - 1

        sq_lst = []
        # square all the values
        sq = [val*val for val in A]
        # sort the values in non-descending order
        while left <= right:
            # add the highest value first
            if sq[left] > sq[right]:
                sq_lst.append(sq[left])
                # move to the next number
                left += 1
            else:
                sq_lst.append(sq_lst[right])
                right -= 1



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** Test Pass! \n")
