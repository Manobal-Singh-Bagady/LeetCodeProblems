class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        mx = 0
        for i in s:
            if i-1 in s:
                continue
            count = 1
            while i+1 in s:
                count+=1
                i+=1
            mx = max(mx,count)
        return mx
