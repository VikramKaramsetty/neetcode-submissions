class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heavy = []
        for i in stones:     
            heapq.heappush(heavy, -i)
        while(len(heavy) > 1):
            stone1 = abs(heapq.heappop(heavy))
            stone2 = abs(heapq.heappop(heavy))
            if(stone1 != stone2):
                val = stone1 - stone2
                heapq.heappush(heavy, -val)
        if(heavy): return -heavy[0]
        return 0
