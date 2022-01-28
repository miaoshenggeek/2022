class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        #Offline Propagation
        qans = [0] * len(positions)
        for i, (left, size) in enumerate(positions):
            right = left + size
            qans[i] += size
            for j in range(i+1, len(positions)):
                left2, size2 = positions[j]
                right2 = left2 + size2
                if left2 < right and left < right2: #intersect
                    qans[j] = max(qans[j], qans[i])
        ans = []
        for x in qans:
            ans.append(max(ans[-1], x) if ans else x)
        return ans
    def ffallingSquares(self, positions: List[List[int]]) -> List[int]:
        #Coordinate Compression
        coords = set()
        for left, size in positions:
            coords.add(left)
            coords.add(left + size)
        index = {x: i for i, x in enumerate(sorted(coords))}
        heights = [0] * len(index)
        def query(L, R):
            return max(heights[i] for i in range(L, R))

        def update(L, R, h):
            for i in range(L, R):
                heights[i] = max(heights[i], h)

        best = 0
        ans = []
        for left, size in positions:
            L = index[left]
            R = index[left + size ]
            h = query(L, R) + size
            update(L, R, h)
            best = max(best, h)
            ans.append(best)

        return ans