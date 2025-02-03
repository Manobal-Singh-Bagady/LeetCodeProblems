class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_inc = 1
        max_dec = 1
        curr_inc = 1
        curr_dec = 1
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                curr_dec+=1
            else:
                curr_dec=1
            max_dec = max(max_dec, curr_dec)
            if nums[i]<nums[i+1]:
                curr_inc+=1
            else:
                curr_inc=1
            max_inc=max(max_inc,curr_inc)
            
        return max(max_inc, max_dec)