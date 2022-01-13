class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """c=collections.Counter(words)
        #return heapq.nlargest(k, c.keys(), key = c.get)#no sorting result
        q=[]
        dic=defaultdict(list)
        for word,count in c.items():
            dic[count].append(word)
        for key in dic:
            heapq.heappush(q,-key)
        #print(dic,q)    
        res=[]
        while q:
            idx=heapq.heappop(q)
            res.extend(sorted(dic[-idx]))
            if len(res)>=k:return res[:k]
        return res"""
        #bucket sort
        bucket=[[] for _ in range(len(words)+1)]  #each pair is count for each word
        c=collections.Counter(words)
        for word,count in c.items():
            bucket[count].append(word)
        res=[]
        for i,wordlist in enumerate(bucket[::-1]):
            res.extend(sorted(wordlist))
            if len(res)>=k:return res[:k]
        return res
        
            
        
            
        
        