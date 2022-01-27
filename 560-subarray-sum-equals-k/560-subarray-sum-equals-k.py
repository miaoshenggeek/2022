class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum=defaultdict(int)
        pre_sum[0]=1
        cur=0
        res=0
        for i in range(len(nums)):
            cur+=nums[i]
            #print(pre_sum)
            if cur-k in pre_sum:
                res+=pre_sum[cur-k]
            pre_sum[cur]+=1
            #print(res)
        return res
        