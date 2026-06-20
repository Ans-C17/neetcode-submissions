class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = [[] for _ in range(n + 1)]
        for u, v, w in times:
            adj_list[u].append((v, w))
        
        dist = [float("inf")] * (n + 1)
        dist[k] = 0
        heap = [(0, k)]

        while heap:
            d, u = heapq.heappop(heap)
            for v, w in adj_list[u]:
                if d + w < dist[v]:
                    dist[v] = d + w
                    heapq.heappush(heap, (dist[v], v))
        
        result = max(dist[1:])
        return result if result != float("inf") else -1
