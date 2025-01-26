class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        longestCycle = 0
        twoCycleInvitations = 0
        inDegree = [0]*n
        depth = [1]*n

        for i in range(n):
            inDegree[favorite[i]]+=1

        q = deque()
        for i in range(n):
            if inDegree[i]==0:
                q.append(i)
        
        while q:
            curr = q.popleft()
            next = favorite[curr]

            depth[next] = max(depth[next], depth[curr]+1)
            inDegree[next]-=1
            if (inDegree[next]==0):
                q.append(next)

        for i in range(n):
            if inDegree[i]==0: continue
            cycleLength = 0
            curr = i
            while (inDegree[curr]!=0):
                inDegree[curr] = 0
                cycleLength+=1
                curr = favorite[curr]
            if cycleLength==2:
                twoCycleInvitations+=depth[i]+depth[favorite[i]]
            else:
                longestCycle = max(longestCycle, cycleLength)
            
        
        return max(longestCycle, twoCycleInvitations)
        