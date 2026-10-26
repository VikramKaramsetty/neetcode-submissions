class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0) + 1
        
        buckets = [[] for _ in range( (len(nums)+1))]
        for k1,v in freq.items():
            buckets[v].append(k1)
        res = []
        for i in range(len(buckets)-1, -1, -1):
            if(len(res) == k): return res
            for j in buckets[i]:
                res.append(j)
