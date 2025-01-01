import math


# score = O(L) + 1(R)
# score = 0(L) + 1(T) - 1(L)
# 1(T) -> Constant
# 0(L)-1(L) -> Variable
# score = ones + best

class Solution:
    def maxScore(self, s: str) -> int:
        ones = 0
        zeros = 0
        best = -math.inf
        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros += 1
            else:
                ones += 1
            best = max(best, zeros - ones)
        if s[-1] == '1':
            ones += 1
        return ones + best
