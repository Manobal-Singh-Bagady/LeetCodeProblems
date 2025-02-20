class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = []
        for i, num in enumerate(nums):
            curr = num[i]
            ans.append("1" if curr == "0" else "0")
        return "".join(ans)
