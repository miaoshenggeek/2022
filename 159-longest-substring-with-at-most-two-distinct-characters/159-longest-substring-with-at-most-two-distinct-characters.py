class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        res=0
        cur={}  #counter
        cnt=0
        l=0
        for r in range(len(s)):
            if s[r] in cur:
                cur[s[r]]+=1
                if cur[s[r]]==1:cnt+=1
            else:
                cur[s[r]]=1
                cnt+=1
            while cnt>2 and l<r:
                cur[s[l]]-=1
                if cur[s[l]]==0:cnt-=1
                l+=1
            
            res=max(res,r-l+1)
        return res
                
                