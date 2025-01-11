class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        odds = 0
        for i in set(s):
            if s.count(i) % 2:
                odds += 1

        return odds <= k and k<=len(s)
