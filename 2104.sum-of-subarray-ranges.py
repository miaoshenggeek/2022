#
# @lc app=leetcode id=2104 lang=python3
#
# [2104] Sum of Subarray Ranges
#
# https://leetcode.com/problems/sum-of-subarray-ranges/description/
#
# algorithms
# Medium (60.21%)
# Likes:    612
# Dislikes: 29
# Total Accepted:    23.2K
# Total Submissions: 38.6K
# Testcase Example:  '[1,2,3]'
#
# You are given an integer array nums. The range of a subarray of nums is the
# difference between the largest and smallest element in the subarray.
# 
# Return the sum of all subarray ranges of nums.
# 
# A subarray is a contiguous non-empty sequence of elements within an array.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3]
# Output: 4
# Explanation: The 6 subarrays of nums are the following:
# [1], range = largest - smallest = 1 - 1 = 0 
# [2], range = 2 - 2 = 0
# [3], range = 3 - 3 = 0
# [1,2], range = 2 - 1 = 1
# [2,3], range = 3 - 2 = 1
# [1,2,3], range = 3 - 1 = 2
# So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.
# 
# Example 2:
# 
# 
# Input: nums = [1,3,3]
# Output: 4
# Explanation: The 6 subarrays of nums are the following:
# [1], range = largest - smallest = 1 - 1 = 0
# [3], range = 3 - 3 = 0
# [3], range = 3 - 3 = 0
# [1,3], range = 3 - 1 = 2
# [3,3], range = 3 - 3 = 0
# [1,3,3], range = 3 - 1 = 2
# So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.
# 
# 
# Example 3:
# 
# 
# Input: nums = [4,-2,-3,4,1]
# Output: 59
# Explanation: The sum of all subarray ranges of nums is 59.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 1000
# -10^9 <= nums[i] <= 10^9
# 
# 
# 
# Follow-up: Could you find a solution with O(n) time complexity?
# 
#

# @lc code=start
from typing import List
import math
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        #find sum of all min for each ele
        n=len(nums)
        nums=[-math.inf]+nums
        mins=[0]*(n+1)
        stack=[0]
        
        for i,ele in enumerate(nums[1:],1):
            while nums[stack[-1]]>ele:
                stack.pop()
            mins[i]=mins[stack[-1]]+ele*(i-stack[-1])
            stack.append(i)

        nums=[math.inf]+nums[1:]
        maxs=[0]*(n+1)
        stack=[0]
        
        for i,ele in enumerate(nums[1:],1):
            while nums[stack[-1]]<ele:
                stack.pop()
            maxs[i]=maxs[stack[-1]]+ele*(i-stack[-1])
            stack.append(i)
            
        return sum(maxs)-sum(mins)


        
# @lc code=end
