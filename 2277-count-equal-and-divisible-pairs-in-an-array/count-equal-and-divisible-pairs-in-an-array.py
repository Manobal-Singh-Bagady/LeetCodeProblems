class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for l in range(n - 1):
            for r in range(l + 1, n):
                if l * r % k == 0 and nums[l] == nums[r]:
                    ans += 1
        return ans
