class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k == (n:=len(s)):
            return True
        if k > n:
            return False

        odds = 0
        for i in set(s):
            if s.count(i) % 2:
                odds += 1
        
        if odds <= k:
            return True
        return False
