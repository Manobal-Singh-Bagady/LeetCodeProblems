class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp = {}
        for i in nums:
            if i not in mp:
                mp[i]=1
            else:
                mp[i]+=1
        N = len(nums)
        for x,y in mp.items():
            if y>N/2:
                return x