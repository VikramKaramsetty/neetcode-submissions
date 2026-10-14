class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {i: amount+3 for i in range(amount+1)}
        dp[0] = 0
        # 0 -> amount
        #dp[1] = 1
        #dp[2] = 1
        #dp[3] = 3
        for i in range(0, amount+1):
            for j in coins:
                if(i - j >= 0):
                    dp[i] = min(dp[i], 1 + dp[i-j])
        
        if(dp[amount] == amount+3): return -1
        return dp[amount]
