class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adjlist = defaultdict(list)
        for u, v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)
        
        edgecount = {}
        leaves = deque()
        for src, neighbours in adjlist.items():
            if len(neighbours) == 1:
                leaves.append(src)
            edgecount[src] = len(neighbours)
        
        while leaves:
            if n <= 2:
                return list(leaves)
            for _ in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for nei in adjlist[node]:
                    edgecount[nei] -= 1
                    if edgecount[nei] == 1:
                        leaves.append(nei)
        return [0]