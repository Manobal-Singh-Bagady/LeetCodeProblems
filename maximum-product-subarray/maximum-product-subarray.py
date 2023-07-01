class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        p = 1
        s = 1
        m = nums[0]
        for i in range(len(nums)):
            p = 1 if p==0 else p
            s = 1 if s==0 else s
            p*=nums[i]
            s*=nums[-(i+1)]
            m = max((m,p,s))
        return m
            
            