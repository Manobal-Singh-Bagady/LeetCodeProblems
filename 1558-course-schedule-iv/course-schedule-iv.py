class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        gr = [[] for _ in range(numCourses)]
        inDegree = [0]*numCourses

        for x, y in prerequisites:
            gr[x].append(y)
            inDegree[y]+=1
        
        q = deque(i for i in range(numCourses) if inDegree[i]==0)
        nodePre = [set() for _ in range(numCourses)]
        while q:
            curr = q.popleft()
            for child in gr[curr]:
                nodePre[child].add(curr)
                for i in nodePre[curr]:
                    nodePre[child].add(i)
                inDegree[child]-=1
                if inDegree[child]==0:
                    q.append(child)
        
        ans = []
        for x, y in queries:
            if x in nodePre[y]:
                ans.append(True)
            else:
                ans.append(False)

        return ans


        