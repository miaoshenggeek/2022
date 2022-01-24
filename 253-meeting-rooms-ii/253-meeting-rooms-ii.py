class Solution:
    def minMeetingRooms(self, A: List[List[int]]) -> int:
        A.sort(key=lambda i: i[0])
        #print(A)
        #sort by start time
        #maintain a min heap of end-time
        q=[]
        res=0
        heapq.heapify(q)
        for i in range(len(A)):
            if q:
                cmp=q[0]
                if q[0]<=A[i][0]:
                    heapq.heappop(q)
            heapq.heappush(q,A[i][1])
            #print(q)
            res=max(res,len(q))
        return res
    #[[6,15],[13,20],[6,17]]
    