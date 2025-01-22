class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]

        row, col = len(isWater), len(isWater[0])
        ans = []
        queue = deque()

        for i in range(row):
            temp = []
            for j in range(col):
                if isWater[i][j]==1:
                    temp.append(0)
                    queue.append((i,j))
                else:
                    temp.append(-1)
            ans.append(temp)
        
        while queue:
            i,j = queue.popleft()
            for dx,dy in dirs:
                x,y = i+dx, j+dy
                if (0<=x<row and 0<=y<col) and ans[x][y] == -1:
                    ans[x][y] = ans[i][j]+1
                    queue.append((x,y))
        return ans




