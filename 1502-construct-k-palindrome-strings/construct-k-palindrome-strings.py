from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        if k == n:
            return True
        if k > n:
            return False
        # map = Counter(s)
        # return sum(1 for i in map if map[i] % 2 != 0) <= k

        freq = [0]*26
        for char in s:
            freq[ord(char)-ord('a')]+=1

        odds = sum(1 for i in freq if i%2)
        return odds<=k
