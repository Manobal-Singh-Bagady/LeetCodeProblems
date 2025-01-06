# Simple solution O(2N)
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0] * n
        
        boxes_left = 0
        steps_left = 0
        boxex_right = 0
        steps_right = 0
        for i in range(n):
            steps_left += boxes_left
            ans[i] += steps_left
            boxes_left += int(boxes[i])
            steps_right += boxex_right
            ans[n - i - 1] += steps_right
            boxex_right += int(boxes[n - i - 1])

        return ans
