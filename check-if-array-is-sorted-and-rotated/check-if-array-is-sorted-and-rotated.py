class Solution:
    def check(self, nums: List[int]) -> bool:
        f = 0
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                f+=1
        if nums[-1]>nums[0]:
            f+=1
        return f<=1

