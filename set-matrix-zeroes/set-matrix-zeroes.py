class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col0 = 1
        for i,x in enumerate(matrix):
            for j,y in enumerate(x):
                if y == 0:
                    if j==0:
                        col0 = 0
                    else:
                        matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[i])):
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j]=0
        if matrix[0][0]==0:
            for i in range(1,len(matrix[0])):
                matrix[0][i]=0
        if col0==0:
            for i in range(len(matrix)):
                matrix[i][0]=0
        
