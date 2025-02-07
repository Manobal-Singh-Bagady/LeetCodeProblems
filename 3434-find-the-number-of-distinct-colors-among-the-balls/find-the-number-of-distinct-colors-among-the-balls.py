class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = {}
        colors = {}
        ans = []
        curr = 0
        for ball,color in queries:
            # balls[i]=color
            # balls[colors[color]]
            # colors[color]=i
            if ball in balls:
                colors[balls[ball]]-=1
                if colors[balls[ball]]==0:
                    del colors[balls[ball]]
            colors[color]=colors.get(color,0)+1
            balls[ball]=color
            ans.append(len(colors))

        return ans
