class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        counts = Counter([num - i for i, num in enumerate(nums)])

        n = len(nums)
        totalCombinations = n * (n - 1) // 2  # nC2 total combinations
        for count in counts.values():
            if count > 1:
                totalCombinations -= (
                    count * (count - 1) // 2
                )  # nC2 combinations are subtracted which are good pairs
        return totalCombinations
