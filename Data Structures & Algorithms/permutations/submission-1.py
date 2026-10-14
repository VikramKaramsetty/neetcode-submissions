class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        def rec(curr):
            if(len(curr) == len(nums)):
                ans.append(curr.copy())
                return
            
            for i in nums:
                if i not in curr:
                    curr.append(i)
                    rec(curr)
                    curr.remove(i)
        rec([])
        return ans
