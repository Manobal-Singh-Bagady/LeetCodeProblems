class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # n = len(nums)
        # indexed = []
        # for i in range(n):
        #     indexed.append((nums[i],i))
        # indexed.sort(key=lambda x:x[0])
        # groups = [[indexed[0][1]]]
        # for i in range(1,n):
        #     if indexed[i][0]-indexed[i-1][0]<=limit:
        #         groups[-1].append(indexed[i][1])
        #     else:
        #         groups.append([indexed[i][1]])
        
        # for group in groups:
        #     sortedVals = sorted([nums[i] for i in group])
        #     sortedGroup = sorted(group)
        #     for i in range(len(group)):
        #         nums[sortedGroup[i]]=sortedVals[i]
        # return nums

        n = len(nums)
        enum = sorted((num,i) for i, num in enumerate(nums))
        groups = [[enum[0]]]
        for i in range(1,n):
            if enum[i][0]-enum[i-1][0]<=limit:
                groups[-1].append(enum[i])
            else:
                groups.append([enum[i]])
        for group in groups:
            vals = sorted([i[0] for i in group])
            idxs = sorted([i[1] for i in group])
            for i in range(len(group)):
                nums[idxs[i]]=vals[i]
        return nums



        