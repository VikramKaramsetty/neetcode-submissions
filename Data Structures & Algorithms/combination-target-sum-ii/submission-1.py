class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        candidates.sort()
        
        def rec(i, curr, total):
            if(total == target):
                if( curr not in ans):
                    ans.append(curr.copy())
            if(total > target): return
            if(i >= len(candidates)): return

            curr.append(candidates[i])
            rec(i+1, curr, total+candidates[i])
            curr.pop()

            val = candidates[i]
            while(i+1< len(candidates) and candidates[i+1] == val):
                i+=1
            rec(i+1, curr, total)


        rec(0, [], 0)
        return ans