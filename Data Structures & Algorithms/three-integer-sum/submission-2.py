class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for fixed in range(len(nums)):
            l, r = fixed+1, len(nums)-1
            if(nums[fixed] > 0): break
            if(fixed > 0 and nums[fixed] == nums[fixed-1]): continue
            while(l < r):
                threeSum = nums[fixed] + nums[r] + nums[l]
                if(threeSum > 0): r-=1
                elif(threeSum < 0): l+=1
                else:
                    res.append([nums[fixed], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return res