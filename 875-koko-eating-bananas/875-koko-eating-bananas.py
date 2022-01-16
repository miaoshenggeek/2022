class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        '''if h==len(piles):return max(piles)
        piles.sort(reverse=True)
        avg=ceil(sum(piles)/h)
        org=avg
        while avg>=piles[-1]:
            piles.pop()
            h-=1
            avg=ceil(sum(piles)/h)
        if avg<=piles[-1]:return piles[h-len(piles)] if 0<h-len(piles)<=len(piles)-1 else org'''
        left=1
        right=max(piles)
        while left<right:
            middle=left+(right-left)//2
            c=0
            for i in piles:
                c+=ceil(i/middle)
            #if c==h:                  #when c==h,still can reduce c
                #return middle
            if c<=h:
                right=middle
            else:
                left=middle+1
        # Once the left and right boundaries coincide, we find the target value,
        return left

        
        
        
        