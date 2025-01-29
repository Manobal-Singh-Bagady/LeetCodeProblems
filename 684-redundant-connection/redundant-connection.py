class Solution:
    def isConnected(self, src, target, visited, gr):
        visited[src] = True

        if src == target:
            return True

        found = False
        for node in gr[src]:
            if not visited[node]:
                found = found or self.isConnected(node, target, visited, gr)
        return found

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        gr = [[] for _ in range(n + 1)]

        for x, y in edges:
            visited = [False] * (n + 1)
            if self.isConnected(x, y, visited, gr):
                return [x, y]

            gr[x].append(y)
            gr[y].append(x)
        return []
