class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bits1 = bin(num1).count("1")
        bits2 = bin(num2).count("1")

        ans = num1
        n = abs(bits2 - bits1)
        i = 0
        set_bit = False if bits2 > bits1 else True
        while n:
            if bool(ans & 1 << i) == set_bit:
                ans ^= 1 << i
                n -= 1
            i += 1
        return ans
