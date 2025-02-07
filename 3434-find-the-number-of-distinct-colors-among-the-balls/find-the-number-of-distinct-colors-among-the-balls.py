class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ans = []

        distinct = 0
        balls = {}
        colors = {}
        for ball, color in queries:
            if ball in balls:
                prevColor = balls[ball]
                colors[prevColor] -= 1
                if colors[prevColor] == 0:
                    distinct -= 1
            balls[ball] = color
            if color in colors:
                colors[color] += 1
            else:
                colors[color] = 1
            if colors[color]==1:
                distinct += 1
            ans.append(distinct)
        return ans
