class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        count = 0
        while nums[0] < k:
            x = heappop(nums)
            y = heappop(nums)
            # Since x is popped before y, x <= y.
            heapq.heappush(nums, x * 2 + y)
            count += 1
        return count
