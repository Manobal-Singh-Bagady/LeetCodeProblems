class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        badPairs = 0
        diffCount = {}
        for i in range(len(nums)):
            badPairs += i - (goodPairs := diffCount.get((diff := nums[i] - i), 0))
            diffCount[diff] = goodPairs + 1
        return badPairs
