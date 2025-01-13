class Solution:
    def minimumLength(self, s: str) -> int:
        freq = [0]*26
        for chr in s:
            freq[ord(chr)-ord('a')]+=1
        
        ans = 0
        for i in freq:
            if i!=0:
                ans+= 1 if i&1 else 2
        return ans            
        