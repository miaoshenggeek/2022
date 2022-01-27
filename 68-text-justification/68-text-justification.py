class Solution:
    def fullJustify(self, words: List[str], W: int) -> List[str]:
        res=[]
        cur=[]
        cnt_lt=0
        for word in words:
            if cnt_lt+len(cur)+len(word)>W:
                #word can't fit in this line
                size=max(1,len(cur)-1)  #number of words in this line
                for i in range(W-cnt_lt): # number of spaces in this line
                    idx=i%size #idx of word in this line
                    cur[idx]+=" "  #add " " after each word to distribut as evenly as possible and left first
                res.append("".join(cur))
                cur=[] #next line
                cnt_lt=0
            cnt_lt+=len(word)
            cur.append(word)
        res.append(" ".join(cur)+" "*(W-cnt_lt-len(cur)+1))
        return res