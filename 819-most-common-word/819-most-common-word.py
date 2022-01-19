class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words=defaultdict(int)
        banned=set(banned)
        cur=""
        for i in paragraph+" ":
            if i.isalpha():
                cur+=i
            else:
                if cur:
                    cur=cur.lower()
                    if not cur in banned:   
                        words[cur]+=1
                cur=""
        #print(words)
        return max(words,key=lambda i: words[i])