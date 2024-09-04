class Solution {
    public void setZeroes(int[][] matrix) {
        List<Integer[]> zeros = new ArrayList<>();
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                if (matrix[i][j] == 0)
                    zeros.add(new Integer[] { i, j });
            }
        }

        for (Integer[] zero : zeros) {
            for (int i = 0; i < matrix.length; i++)
                matrix[i][zero[1]] = 0;
            for (int i = 0; i < matrix[0].length; i++)
                matrix[zero[0]][i] = 0;

        }
    }
}