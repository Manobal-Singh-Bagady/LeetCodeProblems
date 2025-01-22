class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        row = len(isWater)
        col = len(isWater[0])
        ans = [[-1]*col for _ in range(row)]
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        queue = []

        for i in range(row):
            for j in range(col):
                if isWater[i][j]==1:
                    ans[i][j]=0
                    queue.append((i,j))
        
        while queue:
            i,j = queue.pop(0)
            for dir in dirs:
                ni = i+dir[0]
                nj = j+dir[1]
                if (0<=ni<row and 0<=nj<col) and ans[ni][nj] == -1:
                    ans[ni][nj] = ans[i][j]+1
                    queue.append((ni,nj))
        return ans




