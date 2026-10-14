class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ans = 0


        def dfs(i,j) -> int:

            directions = ( (0,1), (1,0), (-1,0), (0,-1))
            total = 0

            for dr, dc in directions:
                row ,col = i+dr, j + dc
                if(0 <= row < len(grid) 
                and 0<= col< len(grid[0])
                and grid[row][col] == 1):
                    grid[row][col] = 0
                    total += dfs(row,col) + 1 

            return total 

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == 1):
                    grid[i][j] = 0 # visited
                    ans = max(ans, dfs(i,j)+1)

        return ans
                
