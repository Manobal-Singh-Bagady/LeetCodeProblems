class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        ans = s
        while (new:=ans.replace(part,'',1))!=ans:
            ans=new
        return ans

        