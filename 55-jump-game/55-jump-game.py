class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:return True
        step=0
        for i in range(len(nums)):
            if nums[i]>step:
                step=nums[i]-1
            else:
                step=step-1
            #print(step)
            if step<0 and i<len(nums)-1:return False
        return True
            
        
        