class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bits1 = bin(num1).count('1')
        bits2 = bin(num2).count('1')

        if bits1==bits2:
            return num1
        elif bits2>bits1:
            ans = num1
            n = bits2-bits1
            i = 0
            while n:
                if not (ans&1<<i):
                    ans ^= 1<<i
                    n-=1
                i+=1
            return ans
        else:
            ans = num1
            n = bits1-bits2
            i = 0
            while n:
                if ans&1<<i:
                    ans ^= 1<<i
                    n-=1
                i+=1
            return ans



                
        
        