class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        if k == n:
            return True
        if k > n:
            return False
        
        freq = [0]*26
        for chr in s:
            freq[ord(chr)-ord('a')]+=1

        odds = 0
        for i in freq:
            if i%2:
                odds+=1
        
        if odds<=k:
            return True
        return False