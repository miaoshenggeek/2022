class Solution:
    def merge(self, A: List[List[int]]) -> List[List[int]]:
        res=[]
        for start,end in sorted(A,key=lambda i: i[0]):
            if not res or res[-1][1]<start:
                res.append([start,end])
            else:
                res[-1][1]=max(res[-1][1],end)
        return res
        
        
                
            
                
        
 