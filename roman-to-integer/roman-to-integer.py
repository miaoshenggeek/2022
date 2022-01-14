class Solution:
    def romanToInt(self, s: str) -> int:
        dic={"I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,} 
        res=0
        #I, VX
        #X, LC
        #C, DM
        for i,v in enumerate(s):
            cur=dic[v]
            if i<len(s)-1 and ((v=="I" and  s[i+1] in "VX") or (v=="X" and  s[i+1] in "LC") or (v=="C" and  s[i+1] in "DM")):
                cur=-cur
            res+=cur
        return res
