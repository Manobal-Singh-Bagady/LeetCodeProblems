class Solution:
    def digitSum(self, num):
        digitSum = 0
        while num:
            digitSum += num % 10
            num //= 10
        return digitSum

    def maximumSum(self, nums: List[int]) -> int:
        digitSums = [0] * 82
        ans = -1
        for num in nums:
            digitSum = self.digitSum(num)
            if digitSums[digitSum] > 0:
                ans = max(ans, digitSums[digitSum] + num)
            digitSums[digitSum] = max(digitSums[digitSum], num)
        return ans
