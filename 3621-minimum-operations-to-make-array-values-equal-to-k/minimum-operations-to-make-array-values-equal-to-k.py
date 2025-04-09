class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        m = min(nums)
        if m < k:
            return -1
        return len(set(nums)) - (m == k)
