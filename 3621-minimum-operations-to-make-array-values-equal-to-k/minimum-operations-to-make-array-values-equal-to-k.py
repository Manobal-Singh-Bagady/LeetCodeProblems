class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if all(i==k for i in nums):
            return 0
        if any(i<k for i in nums):
            return -1
        ans = set()
        for i in nums:
            if i>k:
                ans.add(i)
        return len(ans) or -1