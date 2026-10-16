class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # bottom up dp

        dp = [[0] * n for _ in range(m)]
        visited = set()
        q = deque()
        q.append((m-1, n-1))
        dp[m-1][n-1] = 1
        visited.add((m-1,n-1))
        while q:
            pr, pc = q.popleft()

            directions = ((-1,0), (0,-1))
            for dr, dc in directions:
                r, c = dr + pr, dc + pc
                rr, cc = pr - dr, pc - dc
                if(0 <= rr < m and 0 <= cc < n):
                    dp[pr][pc] += dp[rr][cc]
                
                if((r,c) not in visited and 0 <= r < m and 0<= c < n): 
                    q.append((r,c))
                    visited.add((r,c))

        return dp[0][0]