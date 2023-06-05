class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1

        x *= sign

        ans = 0
        while x > 0:
            ans = ans*10 + x%10
            x //= 10

        if ans*sign < -2**31 or ans*sign > (2**31-1):
            return 0
        else:
            return ans*sign