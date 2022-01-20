class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s: return 0
        res=1
        n=len(s)
        start=0
        end=0
        loc=defaultdict(int)
        loc[s[start]]=start
        while end<n-1:
            end+=1
            if s[end] in loc and loc[s[end]]>=start:
                start=loc[s[end]]+1   
            else:
                res=max(end-start+1,res)
            loc[s[end]]=end
            #print(res,start,end,loc)
        return res
'''
"pwwkew"
"tmmzuxt"
"dvdf"
""
"a"
"au"
'''