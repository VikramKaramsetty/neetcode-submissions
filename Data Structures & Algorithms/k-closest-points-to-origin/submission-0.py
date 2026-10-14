class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        euclid = [(x**2 + y**2, [x,y]) for x,y in points]
        heapq.heapify(euclid)
        for _ in range(k):
            res.append(heapq.heappop(euclid)[1])
        return res