class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = dict()
        for i in s:
            count[i] = count.get(i, 0)+1
        
        for i in range(len(s)):
            if count[s[i]]==1:
                return i
        return -1
        