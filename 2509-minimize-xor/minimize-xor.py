class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bits1 = bin(num1).count("1")
        bits2 = bin(num2).count("1")

        ans = num1
        n = abs(bits2 - bits1)
        i = 0
        if bits2 > bits1:
            set_bit = False
            # while n:
            #     if not (ans & 1 << i):  # check if bit is unset
            #         ans ^= 1 << i       # flip unset bit
            #         n -= 1
            #     i += 1
        elif bits1 > bits2:
            set_bit = True
        while n:
            if bool(ans & 1 << i)==set_bit:        # check if bit is set
                ans ^= 1 << i       # flip set bit
                n -= 1
            i += 1
        return ans
