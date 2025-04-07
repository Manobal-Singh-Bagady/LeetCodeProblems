class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s & 1:
            return False
        dp = set([0])

        for i in nums:
            dp.update([i + num for num in dp])

        return s // 2 in dp
