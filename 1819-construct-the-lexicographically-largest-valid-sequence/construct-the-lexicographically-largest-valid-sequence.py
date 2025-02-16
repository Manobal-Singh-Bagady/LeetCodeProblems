class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        ans = [0] * (2 * n - 1)
        used = set()

        def generateSeq(i: int) -> bool:
            if i == (2 * n - 1):
                return True
            if ans[i]:
                return generateSeq(i + 1)
            for num in range(n, 0, -1):
                if num in used:
                    continue
                nextIndex = i if num == 1 else num + i
                if num > 1 and (nextIndex >= (2 * n - 1) or ans[nextIndex] != 0):
                    continue
                ans[i] = ans[nextIndex] = num
                used.add(num)
                if generateSeq(i + 1):
                    return True
                ans[i] = ans[nextIndex] = 0
                used.remove(num)
            return False

        generateSeq(0)
        return ans
