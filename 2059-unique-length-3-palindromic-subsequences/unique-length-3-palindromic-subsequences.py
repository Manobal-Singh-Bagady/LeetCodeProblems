class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        for letter in set(s):
            l, r = s.index(letter)+1, s.rindex(letter)
            between = set()
            for i in range(l, r):
                if s[i] not in between:
                    ans+=1
                    between.add(s[i])
        return ans

