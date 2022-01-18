class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        arr=sorted(list(zip(username,timestamp,website)))
        #print(arr)
        pattern=[]
        user=arr[0][0]
        pattern=[]
        start=0
        cur=[]
        while start<len(arr):
            
            if arr[start][0]==user:
                cur.append(arr[start][2])
            if not arr[start][0]==user or start==len(arr)-1:
                if len(cur)>=3:
                    pattern.append(cur)
                    
                user=arr[start][0]
                cur=[arr[start][2]]
            start+=1
            
        res=[]
        #print(pattern)
        for cur in pattern:
            if len(cur)>3:
                temp=set(itertools.combinations(cur,3))
                res.extend(list(temp))
            else:
                res.append(tuple(cur))
        #print(res)
        if len(res)==1:return res[0]
        c=Counter(tuple(res))
        #print(c)
        return min(c.items(),key=lambda i:(-i[1],i[0]))[0]
                            