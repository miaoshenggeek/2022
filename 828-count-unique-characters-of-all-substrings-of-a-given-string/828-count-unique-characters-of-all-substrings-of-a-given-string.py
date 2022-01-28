class Solution:
    def uniqueLetterString(self, s: str) -> int:
        """
        OPTIMIZATION:
        Since we only need last_seen and sec_last_seen, we need 2d array with second dimension with len=2. 
        For dp table, we only refer to dp[i-1], so we can just use a simple counter
        Time: O(n)
        Space: O(26 * 2) = O(n)"""
               
        # last_seens[0] is sec previous seen, last_seens[1] is previous seen.
        
        last_seens = [[-1, -1] for _ in range(26)]
        unique_count = 0
        dp = 0

        for i, c in enumerate(s):
            idx = ord(c) - ord('A')   #list indices must be integers or slices, not str
            dp_new = dp + (i - last_seens[idx][1]) - (last_seens[idx][1] - last_seens[idx][0])
            #divide substring with prev and prevof prev, plus cur to prev, minus prev to pop
            last_seens[idx] = [last_seens[idx][1], i]
            dp = dp_new
            unique_count += dp

        return unique_count
        '''
        index = {c:[-1, -1] for c in string.ascii_uppercase}
        res = 0
        for i, ch in enumerate(s):
            k, j = index[ch]
            res += (i - j) * (j - k)
            index[ch] = [j, i]
        # print(index)
        for c in index:
            k, j = index[c]
            res += (len(s) - j) * (j - k)
        return res'''
        
        
     #brute force   
"""class Solution:
    def uniqueLetterString(self, s: str) -> int:        
        n=count=len(s)
        for i in range(n):
            new=set(s[i])
            acount=1
            copy=set()
            for j in range(i+1,n):
                if s[j] in new: 
                    acount-=1
                    if s[j] in copy:acount+=1
                    copy.add(s[j])
                    if acount<0:acount=0
                else:
                    acount+=1
                new.add(s[j])
                
                count+=acount
                #print(acount)
        return count"""
                
        
        
        
    