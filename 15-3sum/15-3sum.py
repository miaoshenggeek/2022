class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #no sort, hashset, O(n^2)
        dup=set()
        seen=dict()
        res=set()
        for i,val1 in enumerate(nums):
            
            if val1 not in dup:
                dup.add(val1)
                for val2 in nums[i+1:]:
                    val3=-val2-val1
                    if val3 in seen and seen[val3]==i:
                        cur=sorted([val1,val2,val3])
                        res.add(tuple(cur))
                    seen[val2]=i
        return res
                
        