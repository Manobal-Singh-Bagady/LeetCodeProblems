class Solution:
    def canPartition(self, square, num):
        if not square:
            return num == 0

        if num < 0:
            return False

        sum = 0
        for i in range(len(square)):
            sum = sum * 10 + int(square[i])
            if sum > num:
                break
            if self.canPartition(square[i + 1 :], num - sum):
                return True
        return False

    def canPartition2(self, square, num):
        if num < 0 or square < num:
            return False

        if square == num:
            return True

        return (
            self.canPartition2(square // 10, num - square % 10)
            or self.canPartition2(square // 100, num - square % 100)
            or self.canPartition2(square // 1000, num - square % 1000)
        )

    def punishmentNumber(self, n: int) -> int:
        ans = 0
        for i in range(1, n + 1):
            squared = i * i
            # if self.canPartition(str(squared), i):
            if self.canPartition2(squared, i):
                ans += squared
        return ans
