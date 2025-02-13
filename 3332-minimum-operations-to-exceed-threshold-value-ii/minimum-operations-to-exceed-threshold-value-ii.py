class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heap = []
        for i in nums:
            heappush(heap,i)
        count = 0
        while heap[0] < k:
            # Since x is popped before y, x <= y.
            heapq.heappush(heap, heappop(heap) * 2 + heappop(heap))
            count += 1
        return count
