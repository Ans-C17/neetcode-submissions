class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        count = 0

        adj = { i: [] for i in range(n) }

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(i):
            if i in visited:
                return
            
            visited.add(i)
            for j in adj[i]:
                dfs(j)
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1

        return count