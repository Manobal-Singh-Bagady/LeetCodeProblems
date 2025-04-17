class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        for l in range(n - 1):
            for r in range(l + 1, n):
                if nums[l] == nums[r] and l * r % k == 0:
                    ans += 1
        return ans
