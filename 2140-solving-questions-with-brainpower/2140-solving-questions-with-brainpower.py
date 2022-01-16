class Solution:
    def mostPoints(self, a: List[List[int]]) -> int:
        n=len(a)
        dp=[0]*200001
        #dp[i] is the largest of dp[i:], dp[i]>=dp[i+1]
        #return dp[0]
        #base case dp[-1]
        dp[n-1]=a[-1][0]
        for i in range(n-2,-1,-1):
            dp[i]=max(a[i][0]+dp[i+a[i][1]+1],dp[i+1])
        return dp[0]
                
        