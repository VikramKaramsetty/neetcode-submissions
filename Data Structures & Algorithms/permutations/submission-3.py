class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        visited = [ False]* len(nums) 
        def rec(curr, visited):
            if(len(curr) == len(nums)):
                ans.append(curr.copy())
                return
            
            for i in range(len(nums)):
                if visited[i] == False:
                    visited[i] = True
                    curr.append(nums[i])
                    rec(curr, visited)
                    visited[i] = False
                    curr.pop()

        rec([], visited)
        return ans
