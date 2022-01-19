class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        zero=0
        start=0
        for i,v in enumerate(nums):
            if v==0:
                zero+=1
            if zero>1:
                
                zero-=1-nums[start]
                start+=1
            
        return i-start+1