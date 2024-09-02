class Solution {
    // void swap(int[] arr, int i, int j) {
    //     int temp = arr[i];
    //     arr[i] = arr[j];
    //     arr[j] = temp;
    // }

    public int removeDuplicates(int[] nums) {
        int l = 0;
        for(int i: nums){
            if(nums[l]!=i) {
                nums[l+1]=i;
                l++;
            }
        }
        return l+1;
    }
}