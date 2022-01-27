class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n==1:return informTime[0]
        dic=defaultdict(list)
        for i,v in enumerate(manager):
            if not v==-1: dic[v].append(i)
        def dfs(i):
            return max([dfs(j) for j in dic[i]] or [0])+informTime[i]
        return dfs(headID)