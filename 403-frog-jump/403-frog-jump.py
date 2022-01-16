class Solution:
    def canCross(self, stones: List[int]) -> bool:
        #DFS
        seen = set()
        stoneSet = set(stones)
        end = stones[-1]
        stack = [(0, 0)] # stone, step
        while len(stack) > 0:
            loc, steps = stack.pop()
            if (loc, steps) in seen:
                continue
            seen.add((loc, steps))
            if loc == end:
                return True
            elif loc < end:
                for i in range(steps-1, steps+2):
                    if i <= 0:
                        continue
                    if loc + i in stoneSet and (loc+i, i) not in seen:
                        stack.append((loc+i, i))
        return False