class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = 0
        count = 0
        ht = {}
        for i in nums:
            if s not in ht:
                ht[s]=1
            else:
                ht[s]+=1
            s+=i
            if s-k in ht:
                count+=ht[s-k]
        return count
