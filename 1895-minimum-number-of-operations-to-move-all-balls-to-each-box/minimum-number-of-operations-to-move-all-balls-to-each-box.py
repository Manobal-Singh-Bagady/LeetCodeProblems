# Simple solution O(2N)
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0]*n
        box_no = 0
        steps = 0
        for i in range(n):
            steps+=box_no
            ans[i]+=steps
            box_no+=int(boxes[i])
        
        box_no = 0
        steps = 0
        for i in range(n):
            steps+=box_no
            ans[n-i-1]+=steps
            box_no+=int(boxes[n-i-1])

        return ans
            




