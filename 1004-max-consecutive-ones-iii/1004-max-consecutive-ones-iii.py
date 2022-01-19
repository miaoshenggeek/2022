class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        '''start=0
        end=1
        cur=1-nums[start]
        res=k
        n=len(nums)
        while end<n:
            while (cur==k and nums[end]==0) or cur>k:
                cur=cur-(1-nums[start])
                start+=1   
            if nums[end]==0 and cur<k:
                cur+=1   
            end+=1
            res=max(res,end-start)
            #print(cur,res,end,start)
        return res'''
        left = right = 0

        for right in range(len(nums)):
            # if we encounter a 0 the we decrement K
            if nums[right] == 0:
                k -= 1
            # else no impact to K

            # if K < 0 then we need to move the left part of the window forward
            # to try and remove the extra 0's
            if k < 0:
                # if the left one was zero then we adjust K
                if nums[left] == 0:
                    k += 1
                # regardless of whether we had a 1 or a 0 we can move left side by 1
                # if we keep seeing 1's the window still keeps moving as-is
                left += 1

        return right - left + 1
        