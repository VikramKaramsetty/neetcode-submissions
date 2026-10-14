class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == 0):
                    q.append((i, j))
        # found all our sources now run bfs

        while(q):
            (i,j) = q.popleft()

            directions = ((0,1), (0,-1), (1,0), (-1,0))
            for dr, dc in directions:
                row,col = dr + i, dc + j
                if(0 <= row < len(grid)
                and 0 <= col < len(grid[0])
                and grid[row][col] == 2147483647):
                    q.append((row,col))
                    grid[row][col] = grid[i][j]+1