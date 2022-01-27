class MedianFinder:

    def __init__(self):
        self.stack=[]
        #self.total=0
        self.cnt=0

    def addNum(self, num: int) -> None:
        idx=bisect_left(self.stack,num)
        self.stack.insert(idx,num)
        #self.total+=num
        self.cnt+=1
        #print(self.stack,self.total,self.cnt,self.total/self.cnt)

    def findMedian(self) -> float:
        if self.cnt%2==1:
            return float(self.stack[self.cnt//2])
        else:
            return (self.stack[self.cnt//2-1]+self.stack[self.cnt//2])/2
    
from heapq import *
class MedianFinder:

    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()