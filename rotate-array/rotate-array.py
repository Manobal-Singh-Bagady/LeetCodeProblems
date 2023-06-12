class Solution:
    def rotate(self, arr: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(arr)
        k %= n
        temp = arr[n - k :]
        for i in range(n-k-1,-1,-1):
            arr[i+k] = arr[i]
        for i in range(k):
            arr[i] = temp[i]