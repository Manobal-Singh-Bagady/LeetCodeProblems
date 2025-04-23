class Solution:
    def countLargestGroup(self, n: int) -> int:
        count = Counter()
        for i in range(1, n+1):
            digitSum = sum(int(x) for x in str(i))
            count[digitSum]+=1
        maxCount =  max(count.values())
        return sum(1 for v in count.values() if v==maxCount)