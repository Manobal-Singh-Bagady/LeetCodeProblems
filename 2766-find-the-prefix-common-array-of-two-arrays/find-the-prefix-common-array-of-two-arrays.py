class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        freq = 0
        count = 0
        ans = []
        for i in range(len(A)):
            if freq & 1 << A[i]:
                count += 1
            freq ^= 1 << A[i]

            if freq & 1 << B[i]:
                count += 1
            freq ^= 1 << B[i]

            ans.append(count)
        return ans
