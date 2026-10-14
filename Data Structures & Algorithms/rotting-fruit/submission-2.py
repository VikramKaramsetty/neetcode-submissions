class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == 2):
                    q.append((i, j))
        minutes = 0
        moved = False
        emptied = False
        while q:
            moved = False
            # level order traversal
            for _ in range(len(q)):
                i,j = q.popleft()
                directions = ((0,1), (1,0) ,(-1,0), (0,-1))
                for dr,dc in directions:
                    row, col= i+dr, j+dc
                    if(0 <= row < len(grid) and
                    0 <= col < len(grid[0])
                    and grid[row][col] == 1):
                        grid[row][col] = 2
                        q.append((row, col))
                        moved = True
            if(moved): minutes+=1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return minutes