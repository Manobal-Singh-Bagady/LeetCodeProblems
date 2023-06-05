class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        w = len(nums) - 1
        l = 0
        r = len(nums) - 1
        l_square = nums[l] ** 2
        r_square = nums[r] ** 2
        while w >= 0:
            if l_square > r_square:
                ans[w] = l_square
                l += 1
                l_square = nums[l] ** 2
            else:
                ans[w] = r_square
                r -= 1
                r_square = nums[r] ** 2
            w -= 1
        return ans