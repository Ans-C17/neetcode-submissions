class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)

            diff = abs(first - second)
            if diff:
                heapq.heappush(heap, -diff)
        
        return -heap[0] if heap else 0