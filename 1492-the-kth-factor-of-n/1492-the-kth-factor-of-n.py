class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        fs=[]
        for i in range(n,0,-1):
            if n%i==0:
                fs.append(i)
        #print(fs)
        return fs[-k] if k<=len(fs) else -1