class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k==0:return 0
        i,j=0,0
        res=0
        cur=0
        seen=defaultdict(int) #cnt
        
        while j<len(s):
            seen[s[j]]+=1
            if seen[s[j]]==1:cur+=1
            while i<j and cur>k:
                seen[s[i]]-=1
                if seen[s[i]]==0:cur-=1
                i+=1
            #print(cur,i,j)
            res=max(res,j-i+1)
            j+=1
        return res
        
                
            
                
            
                                     