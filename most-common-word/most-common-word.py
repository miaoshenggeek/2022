class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words=[]
        cur=""
        for i in paragraph+" ":
            if i.isalpha():
                cur+=i
            else:
                if cur:words.append(cur.lower())
                cur=""
        print(words)
        c=Counter(words)
        for i in banned:
            del c[i]
        return max(c,key=lambda i: c[i])