class Solution:
    def countDigits(self, n):
        count = 0
        while n:
            count += n % 10
            n //= 10
        return count

    def countLargestGroup(self, n: int) -> int:
        mpp = defaultdict(int)
        for i in range(1, n + 1):
            mpp[self.countDigits(i)] += 1
        return list(mpp.values()).count(max(mpp.values()))
