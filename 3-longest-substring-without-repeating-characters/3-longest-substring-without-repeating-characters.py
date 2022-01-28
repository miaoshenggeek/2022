class Solution:
    def lengthOfLongestSubstring(self, s):
        left=0
        res=0
        seen=defaultdict(int)
        for right in range(len(s)):
            if s[right] in seen and seen[s[right]]+1>left:
                left=seen[s[right]]+1
            else:
                res=max(res,right-left+1)
            seen[s[right]]=right    
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