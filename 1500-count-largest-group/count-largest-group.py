class Solution:
    def countLargestGroup(self, n: int) -> int:
        count = Counter()
        for i in range(1, n+1):
            digitSum = sum(list(map(int, list(str(i)))))
            count[digitSum]+=1
        maxCount =  max(count.values())
        ans = 0
        for k, v in count.items():
            if v == maxCount:
                ans+=1
        return ans