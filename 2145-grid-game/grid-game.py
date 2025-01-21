import math

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        firstRowSum = sum(grid[0])
        secondRowSum = 0
        ans = math.inf
        for i in range(len(grid[0])):
            firstRowSum -= grid[0][i]

            result = max(firstRowSum, secondRowSum)
            # ans = min(ans, max(firstRowSum, secondRowSum))
            if result<=ans:
                ans = result
            else:
                return ans
            secondRowSum+=grid[1][i]
        return ans


        