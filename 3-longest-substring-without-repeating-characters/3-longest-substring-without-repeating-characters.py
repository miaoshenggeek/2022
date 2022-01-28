class Solution:
    def lengthOfLongestSubstring(self, s):
        left=0
        res=0
        seen=defaultdict(int)
        for right in range(len(s)):
            if s[right] in seen:
                left=max(left,seen[s[right]]+1)
            seen[s[right]]=right    
            res=max(res,right-left+1)
            #print(left,right,res)
            #print(seen)
        return res
                
'''
"pwwkew"
"tmmzuxt"
"dvdf"
""
"a"
"au"
'''