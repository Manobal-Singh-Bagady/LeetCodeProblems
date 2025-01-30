class DSU:
    def __init__(self, n):
        self.size = [1]*(n+1)
        self.parent = list(range(n+1))

    def find(self, node):
        if self.parent[node]!=node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)

        if u==v:
            return False
        if self.size[u]>self.size[v]:
            self.parent[v]=u
            self.size[u]+=self.size[v]
        else:
            self.parent[u]=v
            self.size[v]+=self.size[u]

class Solution:
    def bfs(self, src, gr, n):
        q = deque()
        visited = [-1]*n
        q.append(src)
        visited[src]+=1
        deepestLayer = 0

        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                for node in gr[curr]:
                    if visited[node]==-1:
                        visited[node]=deepestLayer+1
                        q.append(node)
                    else:
                        if visited[node]==deepestLayer:
                            return -1
            deepestLayer+=1
        return deepestLayer
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        gr = [[] for _ in range(n)]
        dsu = DSU(n)

        for x, y in edges:
            gr[x-1].append(y-1)
            gr[y-1].append(x-1)
            dsu.union(x-1,y-1)

        componentToGroup = {}

        for node in range(n):
            noOfGroups = self.bfs(node, gr, n)
            if noOfGroups ==-1:
                return -1
            root = dsu.find(node)
            componentToGroup[root]=max(componentToGroup.get(root, 0), noOfGroups)
        return sum(componentToGroup.values())


        