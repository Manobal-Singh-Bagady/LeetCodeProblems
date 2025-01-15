class Solution:
    def check_setbit(self, num: int, bit: int) -> bool:
        return num & 1 << bit

    def flip_bit(self, num: int, bit: int) -> int:
        return num ^ 1 << bit

    def minimizeXor(self, num1: int, num2: int) -> int:
        bits1 = bin(num1).count("1")
        bits2 = bin(num2).count("1")

        if bits1 == bits2:
            return num1
        elif bits2 > bits1:
            ans = num1
            n = bits2 - bits1
            i = 0
            while n:
                if not self.check_setbit(ans, i):
                    ans = self.flip_bit(ans, i)
                    n -= 1
                i += 1
            return ans
        else:
            ans = num1
            n = bits1 - bits2
            i = 0
            while n:
                if self.check_setbit(ans, i):
                    ans = self.flip_bit(ans, i)
                    n -= 1
                i += 1
            return ans
