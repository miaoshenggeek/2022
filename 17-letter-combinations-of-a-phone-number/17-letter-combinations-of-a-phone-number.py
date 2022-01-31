class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        adj={'2':["a","b","c"],
             '3':['d','e','f'],
             '4':['g','h','i'],
             '5':['j','l','k'],
             '6':['m','n','o'],
             '7':['p','q','r','s'],
             '8':['t','u','v'],
             '9':['w','x','y','z']
            }
        #bfs
        def bfs():
            if not digits:return 
            n=len(digits)
            res=deque(adj[digits[0]])
            for i in digits[1:]:
                a=len(res)
                for _ in range(a):
                    cur=res.popleft()
                    for j in adj[i]:
                        res.append(cur+j)
            return list(res)
        return bfs()
            