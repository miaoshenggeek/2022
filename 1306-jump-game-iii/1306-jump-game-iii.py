class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if not 0 in arr:return False
        que=deque([start])
        seen=set()
        while que:
            idx=que.popleft()
            num=arr[idx]
            if num==0:return True
            if idx in seen:
                continue 
            
            if idx+num<len(arr):que.append(idx+num) 
            if idx-num>=0:que.append(idx-num) 
            seen.add(idx)
        return False