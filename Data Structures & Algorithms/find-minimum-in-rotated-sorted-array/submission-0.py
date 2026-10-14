class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while(l <= r):
            mid = (l +r )//2
            if(nums[l] < nums[r]):
                #normal list
                return nums[l]
            if(nums[l] > nums[mid]):
                r = mid
            elif(nums[l] <= nums[mid]):
                l = mid+1
        return nums[mid]