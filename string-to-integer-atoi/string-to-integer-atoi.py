class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip(" ")
        res=0
        base=1
        start=0
        for i in s:
            if res==0 and start==0 and i=="0":
                start=1
                continue
            if i=="-" and res==0 and start==0:
                base=-1
                start=1
                continue
            if i=="+" and res==0 and start==0:
                start=1
                base=1
                continue
            if i.isdigit():
                res=res*10+int(i)
            else:
                break
        res*=base 
        if res<-2**31:
            res=-2**31
        elif res>2**31-1:
            res=2**31-1
        return res
            
                