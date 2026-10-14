class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        memo = {n:1}
        if(s[n-1] == 0): memo[n-1] = 0
        else: memo[n-1] = 1
        for i in range(n-1, -1, -1):
            if(s[i] == "0"): 
                memo[i]= 0
                continue
            memo[i] = memo[i+1] 

            if(i+1< n and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456"))):
                memo[i] += memo[i+2]

        return memo[0]
