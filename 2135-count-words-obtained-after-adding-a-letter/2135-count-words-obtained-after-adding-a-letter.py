class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        
        def getHash(w: str) -> List[int]:
            h = [0] * 26
            for c in w:
                h[ord(c) - ord('a')] = 1
            return h
        
        groups = defaultdict(set)
        for w in startWords:
            h = getHash(w)
            groups[len(w)].add(tuple(h))
        cnt = 0
        for w in targetWords:
            h = getHash(w)
            for c in w:
                h[ord(c) - ord('a')] = 0
                if tuple(h) in (groups[len(w) - 1]):
                    cnt += 1
                    break
                h[ord(c) - ord('a')] = 1
        return cnt