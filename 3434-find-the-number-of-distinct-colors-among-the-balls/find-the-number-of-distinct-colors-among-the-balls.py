class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = {}
        colors = {}
        ans = []
        for ball, color in queries:
            if ball in balls:
                prevColor = balls[ball]
                colors[prevColor] -= 1
                if colors[prevColor] == 0:
                    colors.pop(prevColor)
            colors[color] = colors.get(color, 0) + 1
            balls[ball] = color
            ans.append(len(colors))

        return ans
