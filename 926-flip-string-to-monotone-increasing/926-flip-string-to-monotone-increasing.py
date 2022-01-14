class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        #flip right 0 to 1
        #flip left 1 to 0
        if not "0" in s or not "1" in s or len(s)==1: return 0
        n=len(s)
        P=[0]*(n+1)
        for i in range(n):
            P[i+1]=P[i]+int(s[i])
        #print(P)
        ans=n
        for i in range(n+1):
            ans=min(ans,n-i-P[n]+2*P[i])
        return ans