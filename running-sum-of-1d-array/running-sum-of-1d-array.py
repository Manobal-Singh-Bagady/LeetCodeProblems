class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
                # ========Submission 1=========
        # ans = []
        # for i in range(len(nums)):
        #     temp = 0
        #     for j in range(i+1):
        #         temp+= nums[j]
        # return ans

        # ============ Submission 2 ==================
        #     ans.append(temp)
        # for i in range(1, len(nums)):
        #     nums[i] = nums[i-1]+nums[i]
        # return nums

        ans = []
        temp = 0
        for i in nums:
            temp += i
            ans.append(temp)
        return ans