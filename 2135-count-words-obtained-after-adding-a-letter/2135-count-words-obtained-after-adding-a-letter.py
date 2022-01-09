class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        seen = set()
        for word in startWords: 
            m = 0
            for ch in word: m ^= 1 << ord(ch)-ord("a")
            
            seen.add(m)
            
        ans = 0 
        for word in targetWords: 
            m = 0 
            for ch in word: m ^= 1 << ord(ch) - ord("a")
            for ch in word: 
                if m ^ (1 << ord(ch)-ord("a")) in seen: 
                    ans += 1
                    break 
        return ans 