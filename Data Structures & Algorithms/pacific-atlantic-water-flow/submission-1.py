class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        cols = len(heights[0])
        rows = len(heights)
        pacific = [[False] * cols for _ in range(rows)]
        atlantic = [[False] * cols for _ in range(rows)]

        def dfs(arr, i,j):
            
            directions = ((0,1), (0,-1), (1,0), (-1,0))
            for dr,dc in directions:
                row,col = dr +i, dc+ j
                if(0<= row < len(heights)
                and 0<= col < len(heights[0])
                and heights[row][col] >= heights[i][j]
                and not arr[row][col]):
                    arr[row][col] = True
                    dfs(arr, row,col)
        
        for i in range(len(heights)):
            for j in range(len(heights[i])):
                if(i == 0 or j == 0): 
                    pacific[i][j] = True
                    dfs(pacific, i, j)
                if(i == len(heights)-1 or j == len(heights[i]) -1):
                    atlantic[i][j] = True
                    dfs(atlantic, i, j)

        ans = []
        for i in range(len(heights)):
            for j in range(len(heights[i])):
                if(atlantic[i][j] and pacific[i][j]):
                    ans.append([i,j])
        return ans
