class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c=collections.Counter(words)
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
        return res
        
            
        
        