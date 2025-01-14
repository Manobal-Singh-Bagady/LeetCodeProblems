class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        freq = [0]*((n:=len(A))+1)
        count = 0
        ans = []
        for i in range(n):
            freq[A[i]]+=1
            freq[B[i]]+=1

            if freq[A[i]]==2:
                count+=1
            if freq[B[i]]==2 and A[i]!=B[i]:
                count+=1
            ans.append(count)
        return ans
        