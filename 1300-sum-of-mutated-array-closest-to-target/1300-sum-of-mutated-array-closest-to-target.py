class Solution:
    def getRes(self,arr,t):
        nums = [t if num >= t else num for num in arr]
        return sum(nums)
    
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        l = 1
        h = max(arr)
        
        while l <= h:
            mid = (h-l)//2 + l
            curr = self.getRes(arr,mid)
            if curr == target:
                return mid
            elif curr < target:
                l = mid+1
            else:
                h = mid-1
        #end loop l<h or l==h
        #print(l,h,mid)
        if abs(self.getRes(arr,l) - target) < abs(self.getRes(arr,h) - target):
            return l
        return h
            
        
        
        