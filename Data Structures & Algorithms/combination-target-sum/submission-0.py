class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def rec(i, curr, total):
            if(total == target): 
                ans.append(curr.copy())
                return
            if(total > target):
                return
            if(i >= len(nums)):
                return
            
            curr.append(nums[i])
            rec(i, curr, total+nums[i])
            curr.pop()
            rec(i+1, curr, total)
        rec(0, [], 0)
        return ans
