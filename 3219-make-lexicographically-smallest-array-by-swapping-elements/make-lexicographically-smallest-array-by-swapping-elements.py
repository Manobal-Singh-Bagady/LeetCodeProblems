class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        sortedNums = sorted(nums)
        curr = 0
        numToGroup = {}
        numToGroup[sortedNums[0]] = curr

        groupToList = {}
        groupToList[curr] = deque([sortedNums[0]])

        for i in range(1, n):
            if sortedNums[i]-sortedNums[i-1]>limit:
                curr+=1
            numToGroup[sortedNums[i]] = curr

            if curr not in groupToList:
                groupToList[curr] = deque()
            groupToList[curr].append(sortedNums[i])
        
        for i in range(n):
            num = nums[i]
            group = numToGroup[num]
            nums[i] = groupToList[group].popleft()
        
        return nums
            



