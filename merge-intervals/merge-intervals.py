class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        ans = []
        s,e = intervals[0]
        for x,y in intervals:
            if x <= e:
                e = max(e, y)
            else:
                ans.append([s, e])
                s = x
                e = y
        ans.append([s, e])
        return ans