class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        indmap = {}
        def dfs(i, old):
            if(i >= len(nums)):
                return 0
            if((i,old) in indmap):
                return indmap[(i,old)]
            val = dfs(i+1, old) #skip
            if(old == -1 or nums[i] > nums[old]):
                val = max(val, 1 + dfs(i+1, i))
            indmap[(i,old)] = val
            return val
        return dfs(0,-1)
