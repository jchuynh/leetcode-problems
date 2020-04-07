# leetcode 30 days of code challenge

# Single Number
# Given a non-empty array of integers, every element appears twice except for 
# one. Find that single one.

# Note: Note: Your algorithm should have a linear runtime complexity. Could you 
# implement it without using extra memory?

# test case:
# Input: [2,2,1]
# Output: 1

# Input: [4,1,2,1,2]
# Output: 4

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
       
        # first thought, create a dictionary        
        num_dict = {}
        
        # for loop through list to add to dictionary       
        for num in nums:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
                
        # if val is = to 1, return the key --> the num               
        for key, val in num_dict.items():
            if val == 1:
                return key
        
        return "No single integer found." # runtime: 2 for loops --> On^2
        
        ## Is there a better way?
        # sort the list in place 
        # see if the num next to it is the same
        # if not then that number is single