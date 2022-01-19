class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        if n<=2:return 0
        #if height decrease then increase, there is a pit
        #if height keeps increasing or decreasing, no pit
        #if height increase then decrease, no pit
        #use stack to save strickly decreasing nums, when the next num increase, pop and count
        #when the next num stays same, renew the position of the bar
        
        stack=[]
        res=0
        for i,v in enumerate(height):
            #print(stack)
            while stack and stack[-1][1]<v:
                base=stack.pop()[1]
                h=min(stack[-1][1],v)-base if stack else 0
                w=i-stack[-1][0]-1 if stack else 0
                res+=h*w
            stack.append((i,v))
            
            #print(res)
        return res
                
            
                    