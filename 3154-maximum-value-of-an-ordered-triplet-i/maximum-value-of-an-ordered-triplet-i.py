class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                for k, num3 in enumerate(nums):
                    if i < j < k:
                        ans = max(ans, (num1-num2)*num3)
        return ans
