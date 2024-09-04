class Solution {
    public int[] rearrangeArray(int[] nums) {
        int[] ans = new int[nums.length];
        int p = 0, n = 1;
        for(int i: nums){
            if(i>=0){
                ans[p] = i;
                p+=2;
            } else {
                ans[n] = i;
                n+=2;
            }
        }
        return ans;
    }

    void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}