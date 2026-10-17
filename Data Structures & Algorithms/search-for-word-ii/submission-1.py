class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def insert(self, word):
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char] 
        curr.endOfWord = True  
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        head = TrieNode()
        for i in words:
            head.insert(i)
        
        visited = set()
        curr = head
        res = []
        value = ""
        def dfs(i,j):
            nonlocal curr
            nonlocal value

            if curr.endOfWord:
                res.append(value)
                curr.endOfWord = False
            
            directions = ((0,1), (0,-1), (-1,0), (1,0))
            
            for dr,dc in directions:
                r,c = i+dr, dc+j

                if(0 <= r < len(board) and 0<=c < len(board[0]) and (r,c) not in visited):
                    if(board[r][c] in curr.children):
                        tmp = curr
                        visited.add((r,c))
                        curr = curr.children[board[r][c]]

                        value += board[r][c]
                        dfs(r,c)
                        value = value[:-1]

                        visited.remove((r,c))
                        curr = tmp
        
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if(board[i][j] in head.children):
                    curr = head.children[board[i][j]]
                    value = board[i][j]
                    visited.add((i,j))
                    dfs(i,j)
                    value = ""
                    visited.remove((i,j))
        return res


      