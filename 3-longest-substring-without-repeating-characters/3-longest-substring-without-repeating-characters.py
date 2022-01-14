class Solution:
    def lengthOfLongestSubstring(self, s):
        l=0
        r=1
        if len(s)<=1:return len(s)
        new=set(s[l])
        maxcount=0
        while l<len(s):
            while r<len(s) and s[r] not in new:
                new.add(s[r])
                r+=1
            #print(new)
            maxcount=max(maxcount,len(new))
            l=l+1
            if l<len(s):new=set(s[l])
            r=l+1
        return maxcount
        
"aab"
"pwwkew"
"dvdf"