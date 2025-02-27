class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maxLen = 1
        inc = 1
        dec = 1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                dec += 1
                inc = 1
            elif nums[i] < nums[i + 1]:
                inc += 1
                dec = 1
            else:
                inc = 1
                dec = 1
            maxLen = max(maxLen, inc, dec)
        return maxLen
