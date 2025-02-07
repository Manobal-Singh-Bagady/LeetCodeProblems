class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = {}
        colors = Counter()
        ans = []
        for ball, color in queries:
            if ball in balls:
                prevColor = balls[ball]
                colors[prevColor] -= 1
                colors += Counter()
            colors[color] += 1
            balls[ball] = color
            ans.append(len(colors))

        return ans
