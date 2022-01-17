class Solution:
    def findBestValue(self, arr: List[int], t: int) -> int:
        '''n=len(arr)
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
        #compare F(lb) with F(lb-1),where F(lb-1)<t
        a=bisect_left(arr,lb,0,n)
        can=sum(arr[:a])+lb*(n-a)
        b=bisect_left(arr,lb-1,0,n)
        can1=sum(arr[:b])+(lb-1)*(n-b)
        return lb if abs(can-t)<abs(can1-t) else lb-1
        '''
        arr.sort()
        s, n = 0, len(arr)
        
        for i in range(n):
            # ans is best to replace everything from i and on. 
            ans = round((t - s)/n)   #use round to return closest integer to float-四舍五入
            # if this number is smaller than i-th number
            # then return this number, as the next one only makes it bigger
            #print(ans)
            if ans <arr[i]: return ans 
            s += arr[i]
            n -= 1
            
        return arr[-1]
            
        
        
        