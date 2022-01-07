class Solution:
    def topKFrequent(self, nums, k):
        
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key = lambda i: count[i])
        
            
            