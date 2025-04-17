class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for l in range(n):
            for r in range(n):
                if l<r and nums[l]==nums[r] and l*r%k==0:
                    ans+=1
        return ans
        