class Solution:
    def bf_longestSubstring(self, s: str, k: int) -> int:
        res=0
        for i in range(len(s)):
            c=[0]*26
            for j in range(i,len(s)):
                c[ord(s[j])-ord("a")]+=1
                if c and min(set(c)-set([0]))>=k:
                    res=max(res,j-i+1)
        return res
    
#divide and conquer
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        for c in set(s):
            if s.count(c) < k:
                return max([self.longestSubstring(t, k) for t in s.split(c)if len(t)>=k] or [0])
        return len(s)
    
    def _longestSubstring(self, s, k):
        if len(s) < k:
            return 0
        c = min(set(s), key=s.count)
        if s.count(c) >= k:
            return len(s)
        return max(self.longestSubstring(t, k) for t in s.split(c))
            
