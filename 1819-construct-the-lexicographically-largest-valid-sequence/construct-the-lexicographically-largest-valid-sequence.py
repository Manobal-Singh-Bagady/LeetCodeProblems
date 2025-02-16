class Solution:
    def generateSequence(
        self, sequence: List[int], used: List[bool], index: int, n: int
    ) -> bool:
        if index == (2*n-1):
            return True
        if sequence[index] != 0:
            return self.generateSequence(sequence, used, index + 1, n)
        for num in range(n, 0, -1):
            if used[num]:
                continue
            nextIndex = index if num == 1 else num + index
            if num > 1 and (nextIndex >= (2*n-1) or sequence[nextIndex] != 0):
                continue
            sequence[index] = sequence[nextIndex] = num
            used[num] = True
            if self.generateSequence(sequence, used, index + 1, n):
                return True
            sequence[index] = sequence[nextIndex] = 0
            used[num] = False
        return False

    def constructDistancedSequence(self, n: int) -> List[int]:
        ans = [0] * (2 * n - 1)
        used = [False] * (n + 1)
        self.generateSequence(ans, used, 0, n)
        return ans
