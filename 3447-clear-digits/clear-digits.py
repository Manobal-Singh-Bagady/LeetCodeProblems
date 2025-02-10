class Solution:
    def clearDigits(self, s: str) -> str:
        s = list(s)
        beg = 0
        for i in range(len(s)):
            if s[i].isnumeric():
                beg-=1
            else:
                s[beg] = s[i]
                beg+=1
        return "".join(s[:beg])