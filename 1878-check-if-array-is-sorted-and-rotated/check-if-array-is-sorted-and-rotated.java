class Solution {
    public boolean check(int[] nums) {
        int i = 0;
        int j = 1;
        int count = 0;
        while (i<nums.length && j<nums.length){
            if(nums[i]>nums[j]) count++;
            i++;
            j++;
        }
        return count<=1 && (count==0 || nums[0]>=nums[nums.length-1]);
    }
}