class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        if(len(nums) == 0): return 0
        i = 0
        while(i < len(nums)):
            k+=1
            i+=1
            while(i < len(nums) and nums[i] == nums[i-1]):
                nums.pop(i)
        return len(nums)