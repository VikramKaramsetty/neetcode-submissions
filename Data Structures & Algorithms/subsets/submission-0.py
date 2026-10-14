class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        subset = []
        def dfs(i):
            if(i >= len(nums)):
                ans.append(subset.copy())
                return 

            dfs(i+1)
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()

        dfs(0)
        return ans