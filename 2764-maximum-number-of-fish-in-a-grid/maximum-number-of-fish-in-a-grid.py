class Solution:
    def countFishBFS(self, grid, visited, i, j, row, col):
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        fishCount = 0

        q = deque()
        # insert the given node in q
        q.append((i, j))
        visited[i][j] = True

        # start bfs
        while q:
            x, y = q.popleft()
            fishCount += grid[x][y]
            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy
                if (
                    0 <= nx < row
                    and 0 <= ny < col
                    and not visited[nx][ny]
                    and grid[nx][ny] > 0
                ):
                    visited[nx][ny] = True
                    q.append((nx, ny))
        return fishCount

    def countFishDFS(self, grid, visited, i, j, row, col):
        if not (0 <= i < row and 0 <= j < col and not visited[i][j] and grid[i][j] > 0):
            return 0
        visited[i][j] = True
        return (
            grid[i][j]
            + self.countFishDFS(grid, visited, i, j + 1, row, col)
            + self.countFishDFS(grid, visited, i + 1, j, row, col)
            + self.countFishDFS(grid, visited, i, j - 1, row, col)
            + self.countFishDFS(grid, visited, i - 1, j, row, col)
        )

    def findMaxFish(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        maxFish = 0

        visited = [[False] * col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                if grid[i][j] > 0 and not visited[i][j]:
                    maxFish = max(
                        maxFish, self.countFishDFS(grid, visited, i, j, row, col)
                    )
        return maxFish
