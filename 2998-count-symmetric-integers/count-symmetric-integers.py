class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for i in range(low, high+1):
            if len(str(i))%2==0:
                numList = list(map(int, list(str(i))))
                if sum(numList[:len(numList)//2])==sum(numList[len(numList)//2:]):
                    ans+=1
        return ans
            
        