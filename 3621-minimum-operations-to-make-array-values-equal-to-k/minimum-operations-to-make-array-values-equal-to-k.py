class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = set()
        for i in nums:
            if i<k:
                return -1
            elif i>k:
                ans.add(i)
        return len(ans)