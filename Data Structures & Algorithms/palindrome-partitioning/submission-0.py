class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        part = []

        def isPalindrome(pal, i , j):
            if(i >= j): return True
            if(pal[i] != pal[j]): return False
            return isPalindrome(pal, i+1, j-1)

        def dfs(i):
            if(i >= len(s)): 
                ans.append(part.copy())
                return 
            for j in range(i, len(s)):
                # include j
                if(isPalindrome(s, i, j)):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        
        dfs(0)
        return ans

