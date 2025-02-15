class Solution:
    def canPartition(self, square, num):
        if not square:
            return num == 0

        for i in range(len(square)):
            if (sum:=int(square[: i + 1])) > num:
                break
            if self.canPartition(square[i + 1 :], num - sum):
                return True
        return False

    def punishmentNumber(self, n: int) -> int:
        ans = 0
        for i in range(1, n + 1):
            if self.canPartition(str(i * i), i):
                ans += i * i
        return ans
