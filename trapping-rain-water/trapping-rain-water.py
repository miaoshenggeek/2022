class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        if n<=2:return 0
        #if height decrease then increase, there is a pit
        #if height keeps increasing or decreasing, no pit
        #if height increase then decrease, no pit
        #use stack to save decreasing nums, when the next num increase, pop last and count
        
        start=height[0]
        stack=[(0,start)]
        res=0
        for i,v in enumerate(height):
            #print(stack)
            if v==start:
                stack.pop()
                stack.append((i,v))
            elif v<start:
                stack.append((i,v))
                start=v
            elif v>start and stack:
                base=stack.pop()[1]
                while stack and stack[-1][1]<=v:
                    h=stack[-1][1]-base
                    w=i-stack[-1][0]-1
                    res+=h*w
                    base=stack[-1][1]
                    stack.pop()
                    print(res)
                if stack and stack[-1][1]> v: 
                    res+=(v-base)*(i-stack[-1][0]-1)
                stack.append((i,v))
                start=v
                #print(res)
        return res
                
            
                    