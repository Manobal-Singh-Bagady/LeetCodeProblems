class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = nums[0]
        sum = 0
        for i in nums:
            sum+=i
            mx = max(mx,sum)
            if sum<0:
                sum = 0
        return mx