class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        # tree = fully connected + acyclic (undirected)
        adj = { i: [] for i in range(n) }
        visited = set()

        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        def dfs(i, prev):
            if i in visited:
                return False
            
            visited.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                
                if not dfs(j, i):
                    return False
            
            return True
        
        return dfs(0, -1) and n == len(visited)