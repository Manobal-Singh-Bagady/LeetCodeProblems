class Solution:
    def check_setbit(self, num: int, bit: int) -> bool:
        return bool(num & 1 << bit)

    def flip_bit(self, num: int, bit: int) -> int:
        return num ^ 1 << bit

    def minimizeXor(self, num1: int, num2: int) -> int:
        bits1 = bin(num1).count("1")
        bits2 = bin(num2).count("1")

        if bits1 == bits2:
            return num1

        ans = num1
        n = abs(bits2 - bits1)
        i = 0
        check_bit = False if bits2 > bits1 else True
        while n:
            if self.check_setbit(ans, i) == check_bit:
                ans = self.flip_bit(ans, i)
                n -= 1
            i += 1
        return ans
