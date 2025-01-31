class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # get valid cell
        def getCell(x, y):
            if x < 0 or y < 0 or x >= n or y >= n:
                return 0
            else:
                return grid[x][y]

        # simple dfs
        def getIslandSize(x, y, color):
            if getCell(x, y) != 1:
                return 0
            grid[x][y] = color
            return (
                1
                + getIslandSize(x, y + 1, color)
                + getIslandSize(x, y - 1, color)
                + getIslandSize(x + 1, y, color)
                + getIslandSize(x - 1, y, color)
            )
            # size = 1
            # if x != 0 and grid[x - 1][y] == 1:
            #     size += getIslandSize(x - 1, y, color)
            # if y != 0 and grid[x][y - 1] == 1:
            #     size += getIslandSize(x, y - 1, color)
            # if x != n - 1 and grid[x + 1][y] == 1:
            #     size += getIslandSize(x + 1, y, color)
            # if y != n - 1 and grid[x][y + 1] == 1:
            #     size += getIslandSize(x, y + 1, color)
            # return size

        sizes = {}
        colorId = 2

        # pre-compute component sizes
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    sizes[colorId] = getIslandSize(i, j, colorId)
                    colorId += 1

        # if no 1 in the grid only the fliped 0 is largest island
        if len(sizes) == 0:
            return 1

        # flip each 0 and check new sizes
        maxSize = max(sizes.values())
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    neighbours = set()
                    newSize = 1
                    if (
                        i != 0
                        and grid[i - 1][j] > 1
                        and grid[i - 1][j] not in neighbours
                    ):
                        neighbour = grid[i - 1][j]
                        neighbours.add(neighbour)
                        newSize += sizes[neighbour]
                    if (
                        j != 0
                        and grid[i][j - 1] > 1
                        and grid[i][j - 1] not in neighbours
                    ):
                        neighbour = grid[i][j - 1]
                        neighbours.add(neighbour)
                        newSize += sizes[neighbour]
                    if (
                        i != n - 1
                        and grid[i + 1][j] > 1
                        and grid[i + 1][j] not in neighbours
                    ):
                        neighbour = grid[i + 1][j]
                        neighbours.add(neighbour)
                        newSize += sizes[neighbour]
                    if (
                        j != n - 1
                        and grid[i][j + 1] > 1
                        and grid[i][j + 1] not in neighbours
                    ):
                        neighbour = grid[i][j + 1]
                        neighbours.add(neighbour)
                        newSize += sizes[neighbour]
                    maxSize = max(maxSize, newSize)
        return maxSize
