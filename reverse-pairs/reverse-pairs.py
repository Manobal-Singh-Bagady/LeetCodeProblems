class Solution:
    count = 0

    def merge(self, arr, low, mid, high):
        l = low
        r = mid + 1
        temp = []
        while l <= mid and r <= high:
            if arr[l] <= arr[r]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[r])
                r += 1
        while l <= mid:
            temp.append(arr[l])
            l += 1
        while r <= high:
            temp.append(arr[r])
            r += 1
        arr[low : high + 1] = temp[:]

    def countPairs(self, arr, low, mid, high):
        r = mid + 1
        for i in range(low, mid + 1):
            while r <= high and arr[i] > 2 * arr[r]:
                r += 1
            self.count += r - (mid + 1)

    def mergesort(self, arr, low, high):
        if low >= high:
            return
        mid = (low + high) // 2
        self.mergesort(arr, low, mid)
        self.mergesort(arr, mid + 1, high)
        self.countPairs(arr, low, mid, high)
        self.merge(arr, low, mid, high)

    def reversePairs(self, nums: list[int]) -> int:
        self.mergesort(nums, 0, len(nums) - 1)
        print(nums)
        return self.count