class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        rowCount = [0]*row
        colCount = [0]*col

        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    rowCount[i]+=1
                    colCount[j]+=1
        ans = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1 and (rowCount[i]>1 or colCount[j]>1):
                    ans+=1
        return ans


        