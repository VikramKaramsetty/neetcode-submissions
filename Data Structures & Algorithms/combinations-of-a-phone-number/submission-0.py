class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        word = ""

        if(digits== ""): return []
        wordmap = {"2" : "abc", "3" : "def", "4": "ghi", "5":"jkl", "6": "mno", "7": "pqrs", "8" : "tuv", "9": "wxyz"}
        def dfs(i):
            nonlocal word
            if(i >= len(digits)):
                ans.append(word)
                return
            for char in wordmap.get(digits[i]):
                tmp =word
                word += char
                dfs(i+1)
                word = tmp
            


        dfs(0)
        return ans