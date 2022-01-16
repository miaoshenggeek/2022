class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def getV(s):
            for i in range(len(s)):
                if not s[i]==0:
                    return int(s[i:])
            return 0
        
        v1=version1.split(".")
        v2=version2.split(".")
        s1=0
        s2=0
        while s1<len(v1) or s2<len(v2):
            c1=getV(v1[s1]) if s1<len(v1) else 0
            c2=getV(v2[s2]) if s2<len(v2) else 0
            if c1==c2:
                s1+=1
                s2+=1
                continue
            return 1 if c1>c2 else -1
        
            
        return 0
            
            
        