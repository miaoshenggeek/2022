class Solution:
    def findMinArrowShots(self, A: List[List[int]]) -> int:
        #count overlapped balloons as one. 
        #count the number of unoverlapped ballons
        #sort by start
        '''A.sort(key=lambda i:i[0])
        #print(A)
        c=1
        start=A[0][0]
        end=A[0][1]
        for i,j in A[1:]:
            if i<=end:
                start=i
                end=min(j,end)          
            else:
                c+=1
                start=i
                end=j
            #print(q)
        return c'''
        
        arrows   = 0
        prev_end = 0
        
        for start, end in sorted(A, key=lambda i:i[1]):
            if not prev_end or start > prev_end:
                arrows += 1
                prev_end = end
        
        return arrows
    
