class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        ans = [0] * (2 * n - 1)
        used = [False] * (n + 1)

        def generateSeq(i: int) -> bool:
            if i == (2 * n - 1):
                return True
            if ans[i]:
                return generateSeq(i + 1)
            for num in range(n, 0, -1):
                if used[num]:
                    continue
                nextIndex = i if num == 1 else num + i
                if num > 1 and (nextIndex >= (2 * n - 1) or ans[nextIndex] != 0):
                    continue
                ans[i] = ans[nextIndex] = num
                used[num] = True
                if generateSeq(i + 1):
                    return True
                ans[i] = ans[nextIndex] = 0
                used[num] = False
            return False

        generateSeq(0)
        return ans
