class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [nums[i]-i for i in range(n)]
        count = Counter(arr)
        totalComb = n*(n-1)/2
        for i in count.values():
            if i!=1:
                totalComb-=i*(i-1)/2
        return int(totalComb)

