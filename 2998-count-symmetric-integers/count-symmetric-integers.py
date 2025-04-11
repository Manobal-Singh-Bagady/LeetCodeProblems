class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for i in range(low, high+1):
            if i<100 and i%11==0:
                ans+=1
            if 1000<=i<10000:
                left = i//1000 + i%1000//100
                right=i%100//10 + i%10
                if left==right:
                    ans+=1

        return ans
            
        