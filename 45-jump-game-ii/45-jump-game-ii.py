class Solution:
    def jump(self, nums: List[int]) -> int:
        cnt=0
        start=end=0
        #we keep two pointers start and end 
        #that record the current range of the starting nodes
        while end<len(nums)-1:
            temp=end
            end=max([nums[i]+i for i in range(start,end+1)])
            start=temp+1
            cnt+=1
        return cnt
        