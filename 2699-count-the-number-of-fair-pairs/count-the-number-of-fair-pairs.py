class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        return sum(
            bisect_right(nums, upper - nums[i], i + 1)
            - bisect_left(nums, lower - nums[i], i + 1)
            for i in range(len(nums))
        )
        