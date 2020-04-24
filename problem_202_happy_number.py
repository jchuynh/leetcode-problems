# Leetcode challenge

""" Write an algorithm to determine if a number is "happy".

    A happy number is a number defined by the following process: Starting with 
    any positive integer, replace the number by the sum of the squares of its 
    digits, and repeat the process until the number equals 1 (where it will stay), 
    or it loops endlessly in a cycle which does not include 1. Those numbers for 
    which this process ends in 1 are happy numbers.

    test case:


    >>> 19
    True

    Explanation: 
    12 + 92 = 82
    82 + 22 = 68
    62 + 82 = 100
    12 + 02 + 02 = 1


"""
class Solution:
    def isHappy(self, n: int) -> bool:
        
        # psuedocode
        # in while loop?
        # input is an integer, split into digits
        # square digits
        # sum of squared integers != 1
            # continue
        # else return True (sum == 1)
    
        
        def sqsum(num):
            total = 0

            while num > 0:
                digit = num % 10 # get one of the digits of n
                total = total + (digit * digit) # sum of the squared digits
                num = num // 10 # to find the next digit 
                # continue until n < = 0

            return total

        seen = set() # set has a faster look-up time
        while sqsum(n) not in seen: 
            result = sqsum(n)
            if result == 1: # if it equals to 1 then it is a happy ture
                return True
            else:
                seen.add(result)
                n = result
        return False
                print(True)

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** Passed!\n")

