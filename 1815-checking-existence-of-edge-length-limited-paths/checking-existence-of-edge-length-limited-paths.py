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
        if self.size[x] > self.size[y]:
            self.parent[x] = y
            self.size[x] += self.size[y]
        else:
            self.parent[y] = x
            self.size[y] += self.size[x]


class Solution:
    def distanceLimitedPathsExist(
        self, n: int, edgeList: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        queries = sorted((w, p, q, i) for i, (p, q, w) in enumerate(queries))
        edgeList = sorted((w, u, v) for u, v, w in edgeList)

        dsu = DSU(n)

        ans = [False] * len(queries)
        li = 0
        for w, p, q, i in queries:
            while li < len(edgeList) and edgeList[li][0] < w:
                _, u, v = edgeList[li]
                dsu.union(u, v)
                li += 1
            ans[i] = dsu.find(p) == dsu.find(q)
        return ans
