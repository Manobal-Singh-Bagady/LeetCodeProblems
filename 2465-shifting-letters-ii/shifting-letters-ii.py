class Solution:
    def shiftingLetters(self, s: str, shifts) -> str:
        n = len(s)

        # array to keep the range of shifting
        shift_arr=[0]*n
        for l, r, inc in shifts:
            shift_arr[l] += (1 if inc else -1)
            if r+1<n:
                shift_arr[r+1] += (-1 if inc else 1)
        
        ans=''
        current_shift = 0
        for i in range(n):
            current_shift+=shift_arr[i]
            current_chr = ord('a') + (ord(s[i])-ord('a')+current_shift)%26
            ans+=chr(current_chr)
        return ans

