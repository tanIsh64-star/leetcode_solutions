class Solution:
    def containsCycle(self, grid):
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        
        def dfs(r, c, pr, pc, char):
            # mark visited
            visited[r][c] = True
            
            # 4 directions
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == char:
                    
                    # if not visited → continue DFS
                    if not visited[nr][nc]:
                        if dfs(nr, nc, r, c, char):
                            return True
                    
                    # if visited AND not parent → cycle found
                    elif (nr, nc) != (pr, pc):
                        return True
            
            return False
        
        # check every cell
        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    if dfs(i, j, -1, -1, grid[i][j]):
                        return True
        
        return False