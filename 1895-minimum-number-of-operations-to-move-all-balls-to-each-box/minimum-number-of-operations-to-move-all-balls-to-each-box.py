class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ones = []
        n=len(boxes)
        for i in range(n):
            if boxes[i]=='1':
                ones.append(i)
        ans = []
        for i in range(n):
            sum = 0
            for ind in ones:
                sum+=abs(ind-i)
            ans.append(sum)
        return ans


