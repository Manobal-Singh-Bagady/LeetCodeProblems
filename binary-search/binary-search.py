class Solution:
    def binarysearch(self, arr, l, h, k):
        if l>h:
            return -1
        mid = (l+h)//2
        if arr[mid]==k:
            return mid
        elif arr[mid]>k:
            return self.binarysearch(arr, l, mid-1, k)
        else:
            return self.binarysearch(arr, mid+1, h, k)
    def search(self, nums: List[int], target: int) -> int:
        return self.binarysearch(nums, 0, len(nums)-1, target)
        