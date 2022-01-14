class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:return 0
        n=len(s)
        rt=1
        res=1
        start=0
        dic={s[0]:0}
        for i in range(1,n):
            if s[i] in dic:
                start=max(dic[s[i]],start)
                res=i-start
                #print(start,i)
            else:
                res+=1
            dic[s[i]]=i
            #print(res)
            rt=max(res,rt)
        return rt
        
"aab"
"pwwkew"
"dvdf"