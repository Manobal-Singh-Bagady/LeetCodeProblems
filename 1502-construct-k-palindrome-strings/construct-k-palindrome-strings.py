class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k == (n:=len(s)):
            return True
        if k > n:
            return False

        odds = 0
        for chr in s:
            odds^=1<<(ord(chr)-ord('a'))
        return bin(odds).count('1')<=k
