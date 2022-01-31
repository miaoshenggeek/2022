class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start=nums[0]
        end=nums[-1]
        l=0
        r=len(nums)-1
        if start<end:
            while l<=r:
                mid=l+(r-l)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            return -1
        else:
            if target>=start: #target>end
                while l<=r:
                    mid=l+(r-l)//2
                    if nums[mid]==target:
                        return mid
                    elif nums[mid]>target:
                        r=mid-1
                    elif nums[mid]<target:  ##
                        if nums[mid]<=end: r=mid-1
                        else:l=mid+1
            elif target<=end:
                while l<=r:
                    mid=l+(r-l)//2
                    if nums[mid]==target:
                        return mid
                    elif nums[mid]>target:  ##
                        if nums[mid]>=start:l=mid+1
                        else:r=mid-1
                    elif nums[mid]<target:
                        l=mid+1
            return -1
                            
                            
                        
                    
                