class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        return sum(f&1 for f in Counter(s).values())<=k<=len(s)
