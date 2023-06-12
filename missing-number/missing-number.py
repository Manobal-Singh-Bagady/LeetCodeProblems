class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x1 = 0
        x2 = 0
        n = len(nums)
        for i in range(n):
            x1 ^= nums[i]
            x2 ^= i+1
        return x1^x2