class Solution {
    public void rotate(int[][] matrix) {
        for (int i = 0; i < matrix.length; i++)
            for (int j =  i; j < matrix[i].length; j++)
                swapMatrix(matrix, i, j, j, i);

        for (int i = 0; i < matrix.length; i++)
            reverse(matrix[i], 0, matrix[i].length - 1);
    }

    void swapMatrix(int[][] arr, int i1, int i2, int j1, int j2) {
        int temp = arr[i1][i2];
        arr[i1][i2] = arr[j1][j2];
        arr[j1][j2] = temp;
    }

    void reverse(int[] arr, int l, int r) {
        while (l < r) {
            swap(arr, l, r);
            l++;
            r--;
        }
    }

    void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}