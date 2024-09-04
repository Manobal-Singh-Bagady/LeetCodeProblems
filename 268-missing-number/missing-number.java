class Solution {
    public int missingNumber(int[] nums) {
        int x1 = 0, x2 = 0;
        for(int i = 0; i<nums.length; i++){
            x1^=nums[i];
            x2^=(i+1);
        }
        return x1^x2;
    }
}