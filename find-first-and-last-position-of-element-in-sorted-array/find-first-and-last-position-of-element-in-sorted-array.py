class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l = 0
        r = n-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]>=target:
                r = mid-1
            else:
                l = mid+1
        if l == n or nums[l]!=target:
            return (-1,-1)
        else:
            first = l
        l = 0
        r = n-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]>target:
                r = mid-1
            else:
                l = mid+1
        return [first, l-1]
            