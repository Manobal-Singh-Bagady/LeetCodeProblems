class Solution:
    def transpose(self, arr):
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i<j:
                    arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        for i in matrix:
            i.reverse()