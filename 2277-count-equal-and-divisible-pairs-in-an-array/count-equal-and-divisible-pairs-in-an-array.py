class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pairs = set()
        for l in range(n):
            for r in range(n):
                if l<r and nums[l]==nums[r] and l*r%k==0:
                    pairs.add((l,r))
        return len(pairs)
        