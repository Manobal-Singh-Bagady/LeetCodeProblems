class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        ans = 0
        for letter in letters:
            i,j = s.index(letter), s.rindex(letter)
            ans+=len(set(s[i+1:j]))
        return ans

            
