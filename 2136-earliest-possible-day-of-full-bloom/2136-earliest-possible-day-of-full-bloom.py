class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        z=list(zip(plantTime,growTime))
        z.sort(key=lambda i:-i[1]) #longest grow time goes first
        rt=0
        start_time=0
        for p,g in z:
            start_time+=p
            rt=max(rt,start_time+g)
        return rt