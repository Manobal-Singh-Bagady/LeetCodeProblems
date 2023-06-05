from math import ceil
class Solution:
    # ----------Solution by MSB----------

    # ==========Brute Force==========
    # def minimizeArrayValue(self, nums: list[int]) -> int:
    # while True:
    #     m = max(nums)
    #     n = nums.index(m)
    #     nums[n]-=1
    #     nums[n-1]+=1
    #     if nums[n-1]>m:
    #         return m

    # ==========Binary Search==========
    # def checkMid(self, arr: list[int], x: int) -> bool:
    #     sum = 0
    #     for i in range(len(arr)):
    #         sum += arr[i]
    #         if sum > (i+1)*x:
    #             return False
    #     return True

    # def minimizeArrayValue(self, nums: list[int]) -> int:
    #     if nums.index(max(nums)) == 0:
    #         return max(nums)
    #     l, r = 0, max(nums)
    #     while l < r:
    #         mid = (l+r)//2
    #         if self.checkMid(nums, mid):
    #             r = mid
    #         else:
    #             l = mid+1
    #     return l

    # ==========Linear Search==========
    def minimizeArrayValue(self, nums: list[int]) -> int:
        return max(ceil(a/(i+1)) for i, a in enumerate(accumulate(nums)))