class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        currLen = 0
        currChars = set()
        ans = []
        for char in s:
            count[char] -= 1
            currChars.add(char)
            currLen += 1
            if count[char] == 0 and all(count[c] == 0 for c in currChars):
                ans.append(currLen)
                currLen = 0
        return ans