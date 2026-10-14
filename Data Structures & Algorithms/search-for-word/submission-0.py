class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        ans = False
        def recurse(curr, i, j):
            nonlocal ans
            if(curr == ""): 
                ans = True
                return
            if(not(0 <= i < len(board) and 0 <= j < len(board[0]))):
                return
            if(ans): return
            
            if(board[i][j] != curr[0]):
                return
            
            if(board[i][j] == curr[0]):
                tmp = board[i][j]
                board[i][j] = "#"
                recurse(curr[1:], i+1, j)
                recurse(curr[1:], i-1, j)

                recurse(curr[1:], i, j+1)
                recurse(curr[1:], i, j-1)
                board[i][j] = tmp

        for i in range(len(board)):
            for j in range(len(board[i])):
                if(board[i][j] == word[0]):
                    recurse(word, i,j)
        return ans