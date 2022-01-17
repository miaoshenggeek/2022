class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        '''d=dict()
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]]=100005
            else:
                d[s[i]]=i
        if min(d.values())==100005:
            return -1
        return min(d.values())'''
        count = collections.Counter(s)
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1
            