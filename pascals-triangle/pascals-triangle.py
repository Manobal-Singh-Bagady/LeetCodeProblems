class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(1,numRows+1):
            temp = [1]
            m = 1
            for j in range(1,i):
                m*=(i-j)
                m//=j
                temp.append(m)
            ans.append(temp)
        return ans



