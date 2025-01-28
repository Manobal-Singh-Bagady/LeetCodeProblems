class Solution:
    def countFish(self, grid, i, j, row, col):
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        fishCount = 0

        q = deque()
        # insert the given node in q
        q.append((i, j))

        # start bfs
        while q:
            x, y = q.popleft()
            fishCount += grid[x][y]
            grid[x][y] = 0
            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] > 0:
                    q.append((nx, ny))
        return fishCount

    def findMaxFish(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        maxFish = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] > 0:
                    maxFish = max(maxFish, self.countFish(grid, i, j, row, col))
        return maxFish
