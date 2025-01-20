class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rowNum = len(mat)
        colNum = len(mat[0])

        numToPos = [0] * (rowNum * colNum + 1)
        for i in range(rowNum):
            for j in range(colNum):
                numToPos[mat[i][j]] = i, j

        rowCount = [0] * rowNum
        colCount = [0] * colNum

        for i in range(rowNum * colNum):
            x, y = numToPos[arr[i]]
            rowCount[x] += 1
            if rowCount[x] == colNum:
                return i
            colCount[y] += 1
            if colCount[y] == rowNum:
                return i
        return -1
