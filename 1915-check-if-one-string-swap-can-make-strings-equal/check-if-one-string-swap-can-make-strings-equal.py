class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # if s1 == s2:
        #     return True

        # diff = sum(1 for a,b in zip(s1,s2) if a!=b)
        # if diff > 2:
        #     return False

        # if Counter(s1) != Counter(s2):
        #     return False
        # return True

        return sum(a != b for a, b in zip(s1, s2)) <= 2 and Counter(s1) == Counter(s2)
