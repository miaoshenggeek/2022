class Solution:
    def findBestValue(self, arr: List[int], t: int) -> int:
        n=len(arr)
        # find closest value so n*v->t
        # t break arr to <t and ==t
        arr.sort()
        ub=max(arr)
        lb=1
        while lb<ub:
            mid=lb+(ub-lb)//2
            a=bisect_left(arr,mid,0,n)
            can=sum(arr[:a])+mid*(n-a) #F(lb)
            if can==t:
                ub=mid
            elif can<t:
                lb=mid+1 #
            elif can>t:
                ub=mid
        #print(can)
        #always return lb , F(lb)>=t
        a=bisect_left(arr,lb,0,n)
        can=sum(arr[:a])+lb*(n-a)
        b=bisect_left(arr,lb-1,0,n)
        can1=sum(arr[:b])+(lb-1)*(n-b)
        return lb if abs(can-t)<abs(can1-t) else lb-1
        
            
        
        
        