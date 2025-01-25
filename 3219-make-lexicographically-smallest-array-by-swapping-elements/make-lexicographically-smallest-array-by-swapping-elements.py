class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        enum = sorted((nums[i],i) for i in range(n))
        groups = [[enum[0]]]
        for i in range(1, n):
            if enum[i][0] - enum[i - 1][0] <= limit:
                groups[-1].append(enum[i])
            else:
                groups.append([enum[i]])
        for group in groups:
            idxs = sorted([i[1] for i in group])
            for i in range(len(group)):
                nums[idxs[i]] = group[i][0]
        return nums
