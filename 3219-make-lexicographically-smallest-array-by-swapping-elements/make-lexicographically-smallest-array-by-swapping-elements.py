class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        sortedNums = sorted(nums)
        curr = 0
        numToGroup = {}
        numToGroup[sortedNums[0]]=curr
        groupIdx = [0]

        for i in range(1,n):
            if sortedNums[i]-sortedNums[i-1]>limit:
                curr+=1
                groupIdx.append(i)
            numToGroup[sortedNums[i]]=curr
        
        ans = []
        for i in nums:
            group = numToGroup[i]
            ans.append(sortedNums[groupIdx[group]])
            groupIdx[group]+=1
        return ans

            



