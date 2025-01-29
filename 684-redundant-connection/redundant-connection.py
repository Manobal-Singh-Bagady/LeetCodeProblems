class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return False

        xSize = self.size[x]
        ySize = self.size[y]

        if xSize > ySize:
            self.parent[y] = x
            self.size[y] += self.size[x]
        else:
            self.parent[x] = y
            self.size[x] += y
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))

        for x, y in edges:
            if not dsu.union(x, y):
                return [x, y]
        return []
