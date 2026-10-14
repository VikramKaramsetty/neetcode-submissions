class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def rec(i, curr):
            if(i >= len(nums)):
                ans.append(curr.copy())
                return

            #one with i incremented by repeats
            # one where i isn't incremented
            curr.append(nums[i])
            rec(i+1, curr)
            curr.pop()

            while(i + 1 < len(nums) and nums[i] == nums[i+1]):
                i+=1
            rec(i+1, curr)

        rec(0, [])
        return ans 
        
