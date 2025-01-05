class Solution:
    def shiftingLetters(self, s: str, shifts) -> str:
        n = len(s)
        shift_arr=[0]*n
        for l, r, inc in shifts:
            shift_arr[l] += (1 if inc else -1)
            if r+1<n:
                shift_arr[r+1] += (-1 if inc else 1)
        
        current_shift = 0
        string = list(s)
        for i in range(n):
            current_shift+=shift_arr[i]
            current_shift%=26
            current_chr=ord(string[i])
            current_chr+=current_shift
            if current_chr>ord('z'):
                current_chr-=26
            if current_chr<ord('a'):
                current_chr+=26
            string[i]=chr(current_chr)
        return ''.join(string)

