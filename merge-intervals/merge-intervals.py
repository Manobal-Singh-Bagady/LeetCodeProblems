class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        ans = []
        s = intervals[0][0]
        e = intervals[0][1]
        for i in intervals:
            if i[0] <= e:
                e = max(e, i[1])
            else:
                ans.append([s, e])
                s = i[0]
                e = i[1]
        ans.append([s, e])
        return ans