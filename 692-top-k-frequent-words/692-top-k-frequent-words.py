class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        #TC:O(n log k)
        #TS:O(n)
        c=collections.Counter(words)
        #return heapq.nlargest(k, c.keys(), key = c.get)#no sorting result
        # heapq.nsmallest(k, Freqs, key=lambda word:(~Freqs[word], word)
        #~Freqs[words] means 'rank the frequencies of words in descending order' 
        #(the first sorting criteria in lambda function);
        # word means 'rank the words with the highest frequencies in their alphabetical order'
        # (the second sorting criteria in lambda function).
        # Finally, nsmallest() returns the [:k] of the result.
        # nsmallest is implemented O(nlgk)# just maintains a heap size k, not n.
        q=[]
        dic=defaultdict(list)
        for word,count in c.items():
            dic[count].append(word)
        for key in dic:             #O(n)
            heapq.heappush(q,-key) 
            #print(dic,q)  
            if len(q)>k:q=heapq.nsmallest(k,q) #O(k log k) maintains a heap size k, not n.
            #q.pop() pop from end, but the end is random, heapq.heappop(q) pop from head
        res=[]
        # customize python heap compare until I see your solution. 
        # Just wrap a class with customize compare function.
        #TBD
        while q:                   #O(k)  
            idx=heapq.heappop(q)   #O(1)
            res.extend(sorted(dic[-idx])) # O(1)
            if len(res)>=k:return res[:k]  #O(1)
        return res
        
        '''#bucket sort
        #TC: O(n)
        #TS: O(n)
        bucket=[[] for _ in range(len(words)+1)]  #each pair is count for each word
        c=collections.Counter(words)
        for word,count in c.items():
            bucket[count].append(word)
        res=[]
        for i,wordlist in enumerate(bucket[::-1]):
            res.extend(sorted(wordlist))
            if len(res)>=k:return res[:k]
        return res'''
        
            
        
            
        
        