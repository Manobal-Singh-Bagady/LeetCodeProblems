class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        char_indices = dict()

        for i, char in enumerate(s):
            if char not in char_indices:
                char_indices[char] = []
            char_indices[char].append(i)

        ans = 0
        for char_index in char_indices.values():
            l = char_index[0] + 1
            r = char_index[-1]
            unique_between = set(s[l:r])
            ans += len(unique_between)
        return ans
