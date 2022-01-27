class MedianFinder:

    def __init__(self):
        self.stack=[]
        self.total=0
        self.cnt=0

    def addNum(self, num: int) -> None:
        idx=bisect_left(self.stack,num)
        self.stack.insert(idx,num)
        self.total+=num
        self.cnt+=1
        #print(self.stack,self.total,self.cnt,self.total/self.cnt)

    def findMedian(self) -> float:
        if self.cnt%2==1:
            return float(self.stack[self.cnt//2])
        else:
            return (self.stack[self.cnt//2-1]+self.stack[self.cnt//2])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()