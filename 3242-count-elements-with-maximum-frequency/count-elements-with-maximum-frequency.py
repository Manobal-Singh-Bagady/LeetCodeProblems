class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = {}
        for i in nums:
            count[i] = count.get(i, 0)+1
        max_count = max(count.values())

        print(count, max_count)
        ans = 0
        for i in count:
            if count[i]==max_count:
                ans+=count[i]
        return ans

        