class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 0
        n = len(nums)
        for i in range(1, n):
            if nums[p]!=nums[i]:
                nums[p+1]=nums[i]
                p+=1

        return (p+1)