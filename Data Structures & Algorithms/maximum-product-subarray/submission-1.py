class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minProd,maxProd = 1,1
        res = -2^31

        for i in nums:
            if(i == 0):
                minProd, maxProd = 1,1

            temp = maxProd
            maxProd = max(minProd * i, maxProd * i, i)
            minProd = min(minProd * i, temp * i, i)
            res = max(res, maxProd)
        return res