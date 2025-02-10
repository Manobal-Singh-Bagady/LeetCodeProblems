class Solution:
    def clearDigits(self, s: str) -> str:
        ans = []
        for i in s:
            if i.isnumeric():
                ans.pop()
            else:
                ans.append(i)
        return "".join(ans)
                
        