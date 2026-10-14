class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        res = 0

        def dfs(n):
            if(n >= len(nums)):
                return 0
            if(n in memo): return memo[n]
            memo[n] = nums[n] + max(dfs(n+2), dfs(n+3))
            return memo[n]

        return max(dfs(0), dfs(1))