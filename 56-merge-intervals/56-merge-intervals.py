class Solution:
    def merge(self, A: List[List[int]]) -> List[List[int]]:
        res=[]
        for start,end in sorted(A,key=lambda i: i[0]):
            if res and res[-1][1]>=start:
                start=res[-1][0]
                end=max(res[-1][1],end)
                res.pop()
            res.append([start,end])
        return res
        
        
                
            
                
        
 