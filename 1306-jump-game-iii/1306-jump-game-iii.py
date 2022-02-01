class Solution:
    def bfs_canReach(self, arr: List[int], start: int) -> bool:
        if not 0 in arr:return False
        que=deque([start])
        seen=set()
        while que:
            idx=que.popleft()
            num=arr[idx]
            if num==0:return True
            if idx in seen:
                continue   
                ###no need to exit here,
                #continue will prevent dup and make sure que get empty finally
            if idx+num<len(arr):que.append(idx+num) 
            if idx-num>=0:que.append(idx-num) 
            seen.add(idx)
        return False
    def canReach(self, arr: List[int], start: int) -> bool:
        def helper(start):
            if 0<=start<len(arr) and start not in seen:
                if arr[start]==0:return True
                seen.add(start)
                return helper(start-arr[start]) or helper(start+arr[start])
            return False
        
        seen=set()
        return helper(start)
        
            