class Solution:
    def getCell(self, x, y, grid):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
            return 0
        else:
            return grid[x][y]

    def getIslandSize(self, x, y, grid, color):
        if self.getCell(x, y, grid) != 1:
            return 0
        grid[x][y] = color
        return (
            1
            + self.getIslandSize(x, y + 1, grid, color)
            + self.getIslandSize(x + 1, y, grid, color)
            + self.getIslandSize(x, y - 1, grid, color)
            + self.getIslandSize(x - 1, y, grid, color)
        )

    def largestIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        sizes = [0, 0]

        # pre-compute component sizes
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    sizes.append(self.getIslandSize(i, j, grid, len(sizes)))

        maxSize = max(sizes)
        for i in range(row):
            for j in range(col):
                if grid[i][j] != 0:
                    continue
                neighbours = set()
                neighbours.add(self.getCell(i, j + 1, grid))
                neighbours.add(self.getCell(i + 1, j, grid))
                neighbours.add(self.getCell(i, j - 1, grid))
                neighbours.add(self.getCell(i - 1, j, grid))
                newSize = 1
                for color in neighbours:
                    newSize+=sizes[color]
                maxSize = max(maxSize,newSize)
        return maxSize
