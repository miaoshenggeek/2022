class Solution:
    def findSmallestRegion(self, regions: List[List[str]], p: str, q: str) -> str:
        def helper(p):
            for region in regions:
                if p in region:
                    return region[0]
        res=[p]
        while p!=helper(p):
            res.append(helper(p))
            p=helper(p)
        #print(res)
        while q not in res:
            q=helper(q)
        return q
        
                    
        
        