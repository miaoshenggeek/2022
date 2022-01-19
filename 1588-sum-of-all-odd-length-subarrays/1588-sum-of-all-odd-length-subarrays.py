class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n=len(arr)
        res=0
        for i in range(n):
            for j in range(0,n-i,2):
                res+=sum(arr[i:i+j+1])
        return res
        