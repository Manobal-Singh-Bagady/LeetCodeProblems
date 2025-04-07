class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2!=0:
            return False
        dp = set()
        dp.add(0)

        for i in nums:
            dp.update([i+num for num in dp])
        if s//2 in dp:
            return True
        return False


        