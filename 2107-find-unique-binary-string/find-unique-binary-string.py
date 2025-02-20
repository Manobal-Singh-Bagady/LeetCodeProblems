class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        count = dict()
        n = len(nums[0])
        for i in range((2**n)):
            count[str(bin(i))[2:].zfill(n)] = 0
        for i in nums:
            count[i] += 1
        for i in count:
            if count[i] == 0:
                return i
