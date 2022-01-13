class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)    # O(n) space and time
        return [j[0] for j in sorted(counter.items(),key=lambda i: (-i[1],i[0]))][:k]
        """heap = []    # max length will be k, so O(k) extra space
        for word,freq in counter.items():    # O(n) time to iterate counter
            heapq.heappush(heap, (freq,word))    # O(logk)
            if len(heap) > k:    # maintain the heap length of k
                print(heap)
                heapq.heappop(heap)    # pop the smallest freq #O(log k)
             
        res=heapq.nsmallest(k,heap,key=lambda i: (-i[0],i[1]))
        print(res)
        return [i[1] for i in res]"""
        
        '''#bucket sort
        #TC: O(n)
        #TS: O(n)
        bucket=[[] for _ in range(len(words)+1)]  #each pair is count for each word
        c=collections.Counter(words)
        for word,count in c.items():
            bucket[count].append(word)
        res=[]
        for i,wordlist in enumerate(bucket[::-1]):
            res.extend(sorted(wordlist))#O(len(wordlist) log )
            if len(res)>=k:return res[:k]
        return res'''
        
            
        
            
        
        