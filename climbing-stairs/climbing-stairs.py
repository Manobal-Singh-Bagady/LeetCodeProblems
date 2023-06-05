class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [0, 1, 2, 3]
        for i in range(4, n+1):
            arr.append(arr[i-1] + arr[i-2])

        return arr[n]