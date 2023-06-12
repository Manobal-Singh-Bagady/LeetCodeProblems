class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i]!=nums[i-1]:
                nums[p]=nums[i-1]
                p+=1
        nums[p]=nums[n-1]
        p+=1
        return p