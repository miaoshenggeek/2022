class Solution:
    def topKFrequent(self, nums, k):
        # bucket sort idea: no frequencies can be more than n
        bucket = [[] for _ in range(len(nums) + 1)] #看成按index排好序的hashmap
        Count = Counter(nums).items()  
        for num, freq in Count: 
            bucket[freq].append(num) 
        flat_list = [item for sublist in bucket for item in sublist]
        return flat_list[::-1][:k]
        
            
            