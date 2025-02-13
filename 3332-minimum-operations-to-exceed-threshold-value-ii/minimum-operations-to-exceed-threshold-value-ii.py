class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        count = 0
        while nums[0] < k:
            # Since x is popped before y, x <= y.
            heapq.heappush(nums, heappop(nums) * 2 + heappop(nums))
            count += 1
        return count
