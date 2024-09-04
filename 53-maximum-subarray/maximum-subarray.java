class Solution {
    public int maxSubArray(int[] nums) {
        int max = nums[0], sum = 0, start = 0, ansStart=0, ansEnd = 0;
        for (int i = 0; i<nums.length;i++) {
            if(sum==0) start = i;
            sum += nums[i];
            if(sum>max){
                max = sum;
                ansStart = start;
                ansEnd = i;
            }
            if (sum < 0)
                sum = 0;
        }
        System.out.println(ansStart + " " + ansEnd);
        return max;
    }
}