class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ans = []

        balls = {}
        colors = {}
        distinct = 0
        for ball, color in queries:
            if ball in balls:
                prevColor = balls[ball]
                colors[prevColor] -= 1
                if colors[prevColor] == 0:
                    distinct -= 1
            balls[ball] = color
            colors[color]=colors.get(color,0)+1
            if colors[color]==1:
                distinct+=1
            ans.append(distinct)
        return ans
