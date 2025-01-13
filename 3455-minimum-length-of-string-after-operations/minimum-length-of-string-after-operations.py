class Solution:
    def minimumLength(self, s: str) -> int:
        freq = Counter(s)
        
        ans = 0
        for i in freq.values():
            ans+= 1 if i&1 else 2
        return ans            
        