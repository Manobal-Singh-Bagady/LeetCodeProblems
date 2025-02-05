class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        return sum(a != b for a, b in zip(s1, s2)) <= 2 and Counter(s1) == Counter(s2)
