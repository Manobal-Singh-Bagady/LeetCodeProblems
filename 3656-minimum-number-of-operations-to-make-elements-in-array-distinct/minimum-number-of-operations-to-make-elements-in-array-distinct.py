class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        count = Counter(nums)
        ans = 0
        i = 0
        while any([c > 1 for c in count.values()]):
            for _ in range(3):
                count[nums[i]] -= 1
                i += 1
                if i >= n:
                    return ans + 1
            ans += 1
        return ans
