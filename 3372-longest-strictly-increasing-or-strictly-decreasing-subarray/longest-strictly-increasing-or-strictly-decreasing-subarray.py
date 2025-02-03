class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maxLen = 1
        curr_inc = 1
        curr_dec = 1
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                curr_dec+=1
            else:
                curr_dec=1
            if nums[i]<nums[i+1]:
                curr_inc+=1
            else:
                curr_inc=1
            maxLen = max(maxLen, curr_inc, curr_dec)
        return maxLen