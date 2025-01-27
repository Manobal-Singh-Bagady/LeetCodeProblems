class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        gr = defaultdict(list)
        inDegree = [0]*numCourses

        for x, y in prerequisites:
            gr[x].append(y)
            inDegree[y]+=1
        
        q = deque(i for i, deg in enumerate(inDegree) if deg==0)

        nodePre = defaultdict(set)
        while q:
            curr = q.popleft()
            for child in gr[curr]:
                nodePre[child].add(curr)
                nodePre[child].update(nodePre[curr])
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



        