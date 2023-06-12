class Solution:
    def check(self, nums: List[int]) -> bool:
        f = 0
        n = len(nums)
        for i in range(1,n):
            if nums[i-1]>nums[i]:
                f+=1
        if nums[n-1]>nums[0]:
            f+=1
        return f<=1

