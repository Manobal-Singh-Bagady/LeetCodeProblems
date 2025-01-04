from collections import defaultdict


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        indices = defaultdict(list)

        for i, char in enumerate(s):
            indices[char].append(i)

        ans = 0
        for ind in indices.values():
            l = ind[0]
            r = ind[-1]
            ans += len(set(s[l + 1 : r]))
        return ans
