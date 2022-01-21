class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):return ""
        target=Counter(t)
        formed=0
        res=[]
        start=0
        source=Counter()
        for i in range(len(s)):
            source.update(s[i])
            if source[s[i]]==target[s[i]]:
                formed+=1
            while formed==len(target) and start<len(s):
                source[s[start]]-=1
                if start<len(s) and source[s[start]]<target[s[start]]:
                    formed-=1
                    #print(start,i)
                    res.append(s[start:i+1])
                start+=1
        #print(res)            
                    
        return min(res,key=len) if res else ""