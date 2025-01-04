class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = dict()
        last = dict()
        for i in range(len(s)):
            letter = s[i]
            if letter not in first:
                first[letter]= i
            last[letter] = i
        
        ans = 0
        for letter in first:
            ans+=len(set(s[first[letter]+1: last[letter]]))
        return ans


            
