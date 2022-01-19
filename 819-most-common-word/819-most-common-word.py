class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words={}
        banned=set(banned)
        cur=""
        for i in paragraph+" ":
            if i.isalpha():
                cur+=i
            else:
                if cur:
                    cur=cur.lower()
                    if not cur in banned:   
                        words.setdefault(cur,0)
                        words[cur]+=1
                cur=""
        
        return max(words,key=words.get)