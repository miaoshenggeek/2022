class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        
        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < n and 0 <= nc < n:
                    yield nr, nc
                    
        def dfs(grid,i,j,idx):
            
            if i<0 or i>=len(grid) or j<0 or j>=len(grid) or (i,j) in seen or not grid[i][j]==1:
                return
            #if grid[i][j]==1:
            seen.add((i,j))
            grid[i][j]=idx

            dfs(grid,i-1,j,idx)
            dfs(grid,i+1,j,idx)
            dfs(grid,i,j-1,idx)
            dfs(grid,i,j+1,idx)
            
        rt={0:0}
        idx=2
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    seen=set()
                    dfs(grid,i,j,idx)
                    rt[idx]=len(seen)
                idx+=1
        ans=max(rt.values())
        for i in range(n):
            for j in range(n):
                if grid[i][j]==0:
                    can={grid[nr][nc] for nr,nc in neighbors(i,j) if grid[nr][nc]>1}
                    ans=max(ans,1+sum(rt[i] for i in can))
            
                
        #print(rt)            
        return ans

    
        
            
            
    
        