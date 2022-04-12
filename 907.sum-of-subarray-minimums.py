#
# @lc app=leetcode id=907 lang=python3
#
# [907] Sum of Subarray Minimums
#

# @lc code=start
import math
from typing import List
class Solution:
    def sumSubarrayMins(self, nums: List[int]) -> int:
        n=len(nums)
        nums=[-math.inf]+nums
        mins=[0]*(n+1)
        stack=[0]
        
        for i,ele in enumerate(nums[1:],1):
            while nums[stack[-1]]>ele:
                stack.pop()
            mins[i]=mins[stack[-1]]+ele*(i-stack[-1])
            stack.append(i)
        return sum(mins)%(10**9+7)
# @lc code=end

