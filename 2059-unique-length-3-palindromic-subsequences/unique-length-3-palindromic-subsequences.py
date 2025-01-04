class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        for letter in set(s):
            l, r = s.index(letter)+1, s.rindex(letter)
            ans+=len(set(s[l:r]))
        return ans

