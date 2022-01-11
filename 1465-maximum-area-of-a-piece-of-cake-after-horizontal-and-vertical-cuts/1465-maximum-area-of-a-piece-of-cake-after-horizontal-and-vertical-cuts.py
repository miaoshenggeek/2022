class Solution:
    def maxArea(self, h: int, w: int, hc: List[int], vc: List[int]) -> int:
        
        hc=[0]+sorted(hc)+[h]
        vc=[0]+sorted(vc)+[w]
        #print(hc,vc)
        hh=max(i[0]-i[1] for i in zip(hc[1:],hc))
        ww=max(i[0]-i[1] for i in zip(vc[1:],vc))
        #print(hh,ww)
        return hh*ww%(1000000007)