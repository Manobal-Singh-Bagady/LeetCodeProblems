class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        diffArr = [num - i for i, num in enumerate(nums)]
        counts = Counter(diffArr)

        n = len(nums)
        totalCombinations = n * (n - 1) // 2
        for count in counts.values():
            if count > 1:
                totalCombinations -= count * (count - 1) // 2
        return totalCombinations
