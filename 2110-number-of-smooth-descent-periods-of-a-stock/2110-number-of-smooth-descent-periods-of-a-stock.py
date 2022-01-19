class Solution:
    def getDescentPeriods(self, p: List[int]) -> int:
        if len(p)==1:return 1
        stack=[p[0]]
        count=1
        res=1
        '''i=1
        while stack:
            prev=stack.pop()
            cur=p[i]
            if prev-cur==1:
                count+=1
                res+=count
            else:
                count=1
                res+=count
            if i< len(p)-1:stack.append(p[i])
            i+=1
        return res'''
        for i in p[1:]:
            if i==stack.pop()-1:
                count+=1
                res+=count
            else:
                count=1
                res+=count
            stack.append(i)
        return res
        
        