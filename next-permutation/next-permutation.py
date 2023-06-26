class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        flag = True
        for i in range(N - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                index = i
                flag = False
                break
        if flag:
            nums[:] = nums[::-1]
        else:
            for i in range(N - 1, index, -1):
                if nums[i] > nums[index]:
                    nums[i], nums[index] = nums[index], nums[i]
                    break
            nums[:] = nums[: index + 1 :] + nums[:index:-1]