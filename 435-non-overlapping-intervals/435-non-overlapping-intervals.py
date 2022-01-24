class Solution:
    def eraseOverlapIntervals(self, A: List[List[int]]) -> int:
        A.sort(key=lambda i: i[1])
        #print(A)
        end=A[0][1]
        rt=0
        for st,ed in A[1:]:
            if st<end:
                rt+=1
                continue
            end=ed
        return rt