class Solution:
    def minimumLength(self, s: str) -> int:
        return sum(1 if i&1 else 2 for i in Counter(s).values())           
        