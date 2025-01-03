class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        sum = 0
        n = len(nums)
        prefixSum = [0]*n
        for i in range(n):
            sum+=nums[n-i-1]
            prefixSum[n-i-1]=sum
        sum = 0
        ans=0
        for i in range(n-1):
            sum+=nums[i]
            if sum>=prefixSum[i+1]:
                ans+=1
        return ans


        