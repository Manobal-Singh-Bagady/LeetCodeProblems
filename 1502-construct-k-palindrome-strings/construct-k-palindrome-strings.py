from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        if k == n:
            return True
        if k > n:
            return False
        map = Counter(s)
        if sum(1 for i in map if map[i] % 2 != 0) > k:
            return False
        else:
            return True
