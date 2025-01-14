class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        freq = 0
        count = 0
        ans = []
        for i in range(len(A)):
            if freq & 1 << A[i]:  # If A[i] bit is already flipped count+=1
                count += 1
            else:
                freq ^= 1 << A[i]  # Flip the A[i] bit of freq

            if freq & 1 << B[i]:  # If B[i] bit is already flipped count+=1
                count += 1
            else:
                freq ^= 1 << B[i]  # Flip the B[i] bit of freq

            ans.append(count)
        return ans
