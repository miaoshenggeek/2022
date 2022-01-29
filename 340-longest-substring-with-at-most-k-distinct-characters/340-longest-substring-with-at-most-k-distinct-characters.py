class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        #if k==0:return 0
        i,j=0,0
        res=0
        seen=defaultdict(int) #cnt
        
        while j<len(s):
            seen[s[j]]+=1
            j+=1
            while i<j and len(seen)>k:
                seen[s[i]]-=1
                if seen[s[i]]==0:del seen[s[i]]
                i+=1
            #print(cur,i,j)
            res=max(res,j-i)
            
        return res
        
                
            
                
            
                                     