class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        freq = 0
        ans = [0]*(n:=len(A))
        for i in range(n):
            if i!=0:
                ans[i]=ans[i-1]
            
            if freq & 1 << A[i]:  # If A[i] bit is already flipped count+=1
                ans[i] += 1
            freq ^= 1 << A[i]  # Flip the A[i] bit of freq

            if freq & 1 << B[i]:  # If B[i] bit is already flipped count+=1
                ans[i] += 1
            freq ^= 1 << B[i]  # Flip the B[i] bit of freq
        return ans
