class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        count, newCount = Counter(nums), Counter()
        major = max(count, key=count.get)
        for i, num in enumerate(nums):
            newCount[num] += 1
            count[num] -= 1
            if (
                count.get(major, 0) > (n - (i + 1)) // 2
                and newCount.get(major, 0) > (i + 1) // 2
            ):
                return i
        return -1
