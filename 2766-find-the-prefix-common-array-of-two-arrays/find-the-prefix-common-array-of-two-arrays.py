class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        freq = 0
        count = 0
        ans = []
        for i in range(len(A)):
            a_bit = 1<<A[i]
            if freq & a_bit:  # If A[i] bit is already flipped count+=1
                count += 1
            else:
                freq ^= a_bit  # Flip the A[i] bit of freq

            b_bit = 1<<B[i]
            if freq & b_bit:  # If B[i] bit is already flipped count+=1
                count += 1
            else:
                freq ^= b_bit  # Flip the B[i] bit of freq

            ans.append(count)
        return ans
