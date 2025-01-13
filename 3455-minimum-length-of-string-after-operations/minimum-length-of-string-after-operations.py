class Solution:
    def minimumLength(self, s: str) -> int:
        return sum(1 if s.count(char)&1 else 2 for char in set(s))           
        