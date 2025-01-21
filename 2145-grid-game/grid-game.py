import math

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        firstRowSum = sum(grid[0])
        secondRowSum = 0
        ans = math.inf
        for turnIdx in range(len(grid[0])):
            firstRowSum -= grid[0][turnIdx]
            bot2 = max(firstRowSum, secondRowSum)
            if bot2<=ans:
                ans = bot2
            else:
                return ans
            secondRowSum+=grid[1][turnIdx]
        return ans


        