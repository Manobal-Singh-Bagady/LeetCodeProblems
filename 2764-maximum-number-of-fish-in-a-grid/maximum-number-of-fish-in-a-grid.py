class Solution:
    def countFishDFS(self, grid, i, j):
        row, col = len(grid), len(grid[0])
        if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] == 0:
            return 0
        temp = grid[i][j]
        grid[i][j] = 0
        return (
            temp
            + self.countFishDFS(grid, i + 1, j)
            + self.countFishDFS(grid, i, j + 1)
            + self.countFishDFS(grid, i, j - 1)
            + self.countFishDFS(grid, i - 1, j)
        )

    def findMaxFish(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        maxFish = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] > 0:
                    maxFish = max(maxFish, self.countFishDFS(grid, i, j))
        return maxFish
