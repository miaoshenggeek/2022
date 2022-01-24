class Solution:
    def findMinArrowShots(self, A: List[List[int]]) -> int:
        #count overlapped balloons as one. 
        #count the number of unoverlapped ballons
        #sort by start
        A.sort(key=lambda i:(i[0],i[1]))
        #print(A)
        q=[A[0]]
        start=q[-1][0]#1
        end=q[-1][1]#6
        
        for i,j in A[1:]:
            if i<=end:
                start=max(i,start)#2 
                end=min(j,end) #6             
                q.pop()    
            else:
                start=i
                end=j
            q.append([start,end])
            #print(q)
        return len(q)
