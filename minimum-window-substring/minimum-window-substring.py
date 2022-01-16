class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(s)<len(t):return ""
        tt=Counter(t) #count of unique chars in t
        uniqt=len(tt) #number of unique chars in t,to shown in the window
        l,r=0,0
        formed=0 #number of unique chars in t shown in the window
        wc={} #count of unique chars in cur window
        ans= (float("inf"),None,None) #window length,left, right
        while r<len(s):
            cha=s[r]
            wc[cha]=wc.get(cha,0)+1
            if cha in tt and wc[cha]==tt[cha]:
                formed+=1
            while l<=r and formed==uniqt:
                if r-l+1<ans[0]:
                    ans=(r-l+1,l,r)
                cha=s[l]
                wc[cha]-=1
                if cha in tt and wc[cha]<tt[cha]:
                    formed-=1
                l+=1
            r+=1
        #print(ans)
        return "" if ans[1]==None else s[ans[1]:ans[2]+1]   #if not ans[1] will include ans[1]==0
            
                    
            
        
                
            
        
            
        