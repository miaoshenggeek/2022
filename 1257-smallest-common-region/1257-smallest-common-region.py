class Solution:
    def findSmallestRegion(self, regions: List[List[str]], p: str, q: str) -> str:
        def helper(p):
            for i,region in enumerate(regions):
                if p in region:
                    return i,region[0]
        res=[p]
        while p!=helper(p)[1]:
            res.append(helper(p)[1])
            p=helper(p)[1]
        #print(res)
        while q not in res:
            q=helper(q)[1]
        return q
        
                    
        
        