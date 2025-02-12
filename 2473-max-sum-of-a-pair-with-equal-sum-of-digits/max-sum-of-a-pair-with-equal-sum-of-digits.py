class Solution:
    def digitSum(self, num):
        digitSum = 0
        while num:
            digitSum+=num%10
            num//=10
        return digitSum
    def maximumSum(self, nums: List[int]) -> int:
        pairs= []
        for i in nums:
            pairs.append((self.digitSum(i),i))
        pairs.sort()

        ans = -1
        for i in range(len(nums)-1):
            s1, num1 = pairs[i]
            s2, num2 = pairs[i+1]
            if s1==s2:
                ans = max(ans, num1+num2)
        return ans