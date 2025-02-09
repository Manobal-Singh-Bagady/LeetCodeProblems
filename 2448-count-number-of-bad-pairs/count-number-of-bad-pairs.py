class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        ans = 0
        diffCount = {}
        for i in range(len(nums)):
            diff = nums[i] - i

            goodPairs = diffCount.get(diff, 0)

            badPairs = i

            ans += badPairs - goodPairs

            diffCount[diff] = goodPairs + 1
        return ans
