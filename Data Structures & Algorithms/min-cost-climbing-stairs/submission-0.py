class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        costs = {}
        res = 0

        def dfs(n) -> int:
            if(n == len(cost)):
                return 0
            elif (n > len(cost)): return pow(2,31)

            if(n in costs): return costs[n]
            costs[n] = min(dfs(n+1) + cost[n], dfs(n+2) + cost[n])
            return costs[n]

        dfs(0)
        dfs(1)
        return min(costs[0], costs[1])