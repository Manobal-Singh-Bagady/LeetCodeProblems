class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        ans = [0] * (2 * n - 1)
        used = [False] * (n + 1)

        def generateSeq(i: int) -> bool:
            if i == len(ans):
                return True
            if ans[i]:
                return generateSeq(i + 1)
            for num in range(n, 0, -1):
                if used[num]:
                    continue
                used[num] = True
                ans[i] = num
                if num == 1:
                    if generateSeq(i + 1):
                        return True
                elif num + i < len(ans) and ans[num + i] == 0:
                    ans[num + i] = num
                    if generateSeq(i + 1):
                        return True
                    ans[num + i] = 0
                ans[i] = 0
                used[num] = False
            return False

        generateSeq(0)
        return ans
