class Solution:
    _dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    def _isValidCell(self, x, y, row, col):
        return 0 <= x < row and 0 <= y < col

    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        row, col = len(isWater), len(isWater[0])
        ans = [[-1] * col for _ in range(row)]
        queue = deque()

        # Mark water cells as 0
        for i in range(row):
            for j in range(col):
                if isWater[i][j] == 1:
                    ans[i][j] = 0
                    queue.append((i, j))

        # BFS
        while queue:
            i, j = queue.popleft()

            # Get all neighbouring cells
            for dx, dy in self._dirs:
                x, y = i + dx, j + dy
                # If un-visited and valid
                if self._isValidCell(x, y, row, col) and ans[x][y] == -1:
                    # height = current+1
                    ans[x][y] = ans[i][j] + 1
                    queue.append((x, y))
        return ans
