class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        visited = set()

        def dfs(i,j):
            nonlocal visited
            #set every sorrounding 1 to visited
            #base case
            if(not(0 <= i< len(grid) and 0<= j < len(grid[0]))):
                return
            
            if(grid[i][j] == "0"): return
            sorroundings = ((0,1), (0,-1),(1,0), (-1,0))

            for (dr, dc) in sorroundings:
                row, col= i + dr, j+dc
                if(0 <= row< len(grid) 
                and 0<= col < len(grid[0])
                and grid[row][col] == "1"
                and (row,col) not in visited
                ): 
                    visited.add( (row,col))
                    dfs(row,col)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == "1" and (i,j) not in visited):
                    visited.add((i,j))
                    dfs(i,j)
                    ans+=1

        return ans