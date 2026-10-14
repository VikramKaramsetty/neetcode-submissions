class Solution:
    def rob(self, nums: List[int]) -> int:
        memoZero = {}
        memoNorm = {}
        res = 0

        def dfs(n, startZero):
            if(startZero and n >= len(nums)-1): return 0
            if(n >= len(nums)):
                return 0
            if(startZero and n in memoZero): return memoZero[n]
            if(not startZero and n in memoNorm): return memoNorm[n]
            val = nums[n] + max(dfs(n+2, startZero), dfs(n+3, startZero))
            
            if(startZero): 
                memoZero[n] = val
                return memoZero[n]
            else: 
                memoNorm[n] = val
                return memoNorm[n]

        return max(nums[0], dfs(0, True), dfs(1, False), dfs(2, False))