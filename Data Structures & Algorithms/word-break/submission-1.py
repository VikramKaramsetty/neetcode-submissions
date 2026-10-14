class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #applepenapple
        #apple pen apple
        #apple dict = [app]
        #apple 
        # app ple 

        memo = {}

        def dfs(i):
            if(i == len(s)):
                return True
            if(i in memo): return memo[i]
            for word in wordDict:
                newLength = i + len(word)
                if(s[i : newLength] == word and dfs(newLength)):
                    memo[i] = True
                    return True
            memo[i] = False
            return False
        return dfs(0)
                    