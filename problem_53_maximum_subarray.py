# Leetcode, 30 days challenge

# Maximum Subarray
# Given an integer array nums, find the contiguous subarray (containing at 
# least one number) which has the largest sum and return its sum.

# test case:
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Kadane's Algorithm Explanation:
# largest sum of contiguous subarray
# start at one point in the array and see if it is the global max
# if it is save that value
# check the next index, then the sum of this current one and the previous one
# see which one is bigger
# continue the process

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # pseudocode: Kadane's Algorithm

        # keep current and global current variable
        # Starting point is at index 0
        max_current = total_max = nums[0]
        
        for i in nums[1:]:
            # the highest value of 
            # the current index
            # or the total_max + the previous index
            total_max = max(i, total_max + i)
            # comparing the current sum to the total_max sum
            max_current = max(max_current, total_max)
             
        return max_current