class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dupe = set(nums)
        longest = 0
        for i in nums:
            if(i-1 not in dupe):
                inc = 1
                while(i+inc in dupe): 
                    inc+=1
                if(inc > longest):
                    longest = inc

        return longest