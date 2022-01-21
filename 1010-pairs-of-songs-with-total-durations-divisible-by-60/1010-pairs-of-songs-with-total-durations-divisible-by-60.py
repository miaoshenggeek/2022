class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        new=[i%60 for i in time]
        #print(new)
        dic=defaultdict(int)  
        res=0
        for i in new:
            c=(60-i)%60 #if i else 0
            if c in dic:
                res+=dic[c]
            dic[i]+=1
        return res