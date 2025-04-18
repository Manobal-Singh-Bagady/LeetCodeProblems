class Solution:
    def rleEncode(self, s: str) -> str:
        newStr = ""
        i = 0
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]:
                count += 1
                i += 1
            newStr += str(count) + s[i]
            i += 1
        return newStr
        
    def countAndSay(self, n: int) -> str:
        ans = "1"
        for i in range(1,n):
            ans = self.rleEncode(ans)
        return ans
        