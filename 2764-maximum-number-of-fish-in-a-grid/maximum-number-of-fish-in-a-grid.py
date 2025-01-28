class Solution:
    def countFishDFS(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return 0
        if grid[i][j] == 0:
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
        maxFish = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    maxFish = max(maxFish, self.countFishDFS(grid, i, j))
        return maxFish
