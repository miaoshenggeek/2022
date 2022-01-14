class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        start=0
        end=n-1
        rt=0
        while start<end:
            if height[start]==0:
                start+=1
            if height[end]==0:
                end-=1
            rt=max(min(height[start],height[end])*(end-start),rt)
            if height[start]<height[end]:start+=1
            else:end-=1
        return rt
            
            