class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        mid = len(nums) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.search(nums[:mid], target)
        elif nums[mid] < target:
            res = self.search(nums[mid+1:], target)
            return -1 if res==-1 else (res+1+mid)