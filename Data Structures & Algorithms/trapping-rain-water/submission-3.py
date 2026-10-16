class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        prefix = [0] * len(height)
        suffix = [0] * len(height)

        maxVal = 0
        for i in range( len(height)):
            maxVal = max(maxVal, height[i])
            prefix[i] = maxVal
        maxVal = 0
        for i in range(len(height)-1, -1,-1):
            maxVal = max(maxVal, height[i])
            suffix[i] = maxVal

        for i in range(len(height)):
            res += abs(min(prefix[i], suffix[i]) - height[i])

        return res
        


