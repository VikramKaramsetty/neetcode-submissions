class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-i for i in count.values()]
        heapq.heapify(heap)

        time = 0
        queue = deque() #[count, time]
        while(heap or queue):
            time+=1
            if(not heap):
                time = queue[0][1]
            else: 
                top = heapq.heappop(heap) +1
                if(top!= 0): queue.append([top, time + n])

            if(queue and queue[0][1] == time):
                heapq.heappush(heap, queue.popleft()[0])
        return time