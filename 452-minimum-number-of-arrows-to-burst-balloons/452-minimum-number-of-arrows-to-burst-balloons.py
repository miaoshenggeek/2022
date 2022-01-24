class Solution:
    def findMinArrowShots(self, A: List[List[int]]) -> int:
        #count overlapped balloons as one. 
        #count the number of unoverlapped ballons
        #sort by start
        A.sort(key=lambda i:(i[0],i[1]))
        #print(A)
        c=1
        start=A[0][0]#1
        end=A[0][1]#6
        for i,j in A[1:]:
            if i<=end:
                start=max(i,start)#2 
                end=min(j,end) #6             
                 
            else:
                c+=1
                start=i
                end=j
            
            #print(q)
        return c
