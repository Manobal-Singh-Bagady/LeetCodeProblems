class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> ans = new ArrayList<>();
        int n = matrix.length;
        int m = matrix[0].length;

        int left = 0, right = m - 1, top = 0, bottom = n - 1;

        while (left <= right && top <= bottom) {

            // moving left to right
            for (int i = left; i <= right; i++)
                ans.add(matrix[top][i]);
            top++;

            // moving top to bottom
            for (int i = top; i <= bottom; i++)
                ans.add(matrix[i][right]);
            right--;

            if (top <= bottom) {
                // moving right to left
                for (int i = right; i >= left; i--)
                    ans.add(matrix[bottom][i]);
                bottom--;
            }

            if(left<=right){
            // moving bottom to top
            for (int i = bottom; i >= top; i--)
                ans.add(matrix[i][left]);
            left++;
            }
        }
        return ans;
    }
}