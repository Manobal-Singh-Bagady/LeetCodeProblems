class Solution:
    def partitionString(self, s: str) -> int:
        count, sub = 1, ''
        for i in s:
            if i in sub:
                count += 1
                sub=i
            else:
                sub+=i
        return count