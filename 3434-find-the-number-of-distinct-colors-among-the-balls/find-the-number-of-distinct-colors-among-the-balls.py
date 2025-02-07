class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = {}
        colors = {}
        ans = []
        distinct = 0
        for ball, color in queries:
            if ball in balls:
                prevColor = balls[ball]
                colors[prevColor] -= 1
                if colors[prevColor] == 0:
                    del colors[prevColor]
                    distinct -= 1
            if color not in colors:
                colors[color] = 0
                distinct += 1
            colors[color] += 1
            balls[ball] = color
            ans.append(distinct)

        return ans
