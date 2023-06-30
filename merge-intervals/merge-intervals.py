class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        ans = []
        s = intervals[0][0]
        e = intervals[0][1]
        for x,y in intervals:
            if x <= e:
                e = max(e, y)
            else:
                ans.append([s, e])
                s = x
                e = y
        ans.append([s, e])
        return ans