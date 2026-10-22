class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(n):
            if(nums[i] < 0): nums[i] = 0

        for i in range(n):
            ind = abs(nums[i])-1
            if(0 <= ind < len(nums)):
                if(nums[ind] == 0): nums[ind] = len(nums)+1
                nums[ind] = abs(nums[ind]) * -1
        
        for i in range(n):
            if(nums[i] >= 0): return i+1

        return n+1
