class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = deque()

        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                if((i == 0 or i == rows-1 or j == 0 or j == cols-1) and board[i][j] == 'O'):
                    q.append((i,j))
                    board[i][j] = 'M'
        
        #now do multi source bfs
        while(q):
            (i,j) = q.popleft()

            directions = ((0,1), (0,-1), (1,0), (-1,0))

            for dr, dc in directions:
                row, col = i+dr, j+dc
                if(0 <= row < rows and 0 <= col < cols
                and board[row][col] == 'O'):
                    q.append((row, col))
                    board[row][col] = 'M'
            
        for i in range(rows):
            for j in range(cols):
                if( board[i][j] == 'M'):
                    board[i][j] = 'O'
                elif(board[i][j] == 'O'):
                    board[i][j] = 'X'
