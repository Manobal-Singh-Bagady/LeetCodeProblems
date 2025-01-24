class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        inDegree = [0] * n

        reverseGraph = [[] for _ in range(n)]

        for i in range(n):
            for node in graph[i]:
                reverseGraph[node].append(i)
                inDegree[i] += 1

        q = deque([i for i in range(n) if inDegree[i] == 0])
        isSafe = [False] * n

        while q:
            node = q.popleft()
            isSafe[node] = True
            for neighbour in reverseGraph[node]:
                inDegree[neighbour] -= 1
                if inDegree[neighbour] == 0:
                    q.append(neighbour)

        return [i for i in range(n) if isSafe[i]]
