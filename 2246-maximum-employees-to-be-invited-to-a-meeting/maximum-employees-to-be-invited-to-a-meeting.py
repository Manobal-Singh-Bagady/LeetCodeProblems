class Solution:
    def maximumInvitations(self, fav: List[int]) -> int:
        n = len(fav)
        longestCycle = 0
        twoCycleInvitations = 0
        inDegree = [0]*n
        depth = [1]*n

        for i in fav:
            inDegree[i]+=1
        q = deque(i for i in range(n) if inDegree[i]==0)
        
        while q:
            curr = q.popleft()
            next = fav[curr]

            depth[next] = depth[curr]+1
            inDegree[next]-=1
            if (inDegree[next]==0):
                q.append(next)

        for i in range(n):
            if inDegree[i]==0: continue
            cycleLength = 1
            inDegree[i]=0
            curr = fav[i]
            while (curr!=i):
                inDegree[curr] = 0
                cycleLength+=1
                curr = fav[curr]
            if cycleLength==2:
                twoCycleInvitations+=depth[i]+depth[fav[i]]
            else:
                longestCycle = max(longestCycle, cycleLength)
            
        
        return max(longestCycle, twoCycleInvitations)
        