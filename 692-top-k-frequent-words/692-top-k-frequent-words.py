class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)    # O(n) space and time
        return heapq.nsmallest(k, counter, key=lambda word:(-counter[word], word))
        #return [j[0] for j in sorted(counter.items(),key=lambda i: (-i[1],i[0]))][:k]  #O (n log n)