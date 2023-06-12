class Solution:
    def rotate(self, arr: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(arr)
        k %= n
        arr[:n-k] = arr[:n-k][::-1]
        arr[n-k:] = arr[n-k:][::-1]
        arr.reverse()