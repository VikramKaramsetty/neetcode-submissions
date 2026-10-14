class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def rec(curr, openP, closeP):
            if(openP + closeP == n*2): 
                ans.append(curr)
                return
            
            if(closeP < openP):
                rec(curr + ")", openP, closeP+1)
            if(openP < n):
                rec(curr + "(", openP+1, closeP)
            
        rec("", 0,0 )
        return ans
        