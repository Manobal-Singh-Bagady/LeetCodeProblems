class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int ans = 0;
        int count = 0;
        for (int i : nums) {
            if (i == 1)
                count++;
            else
                count = 0;
            ans = Math.max(count, ans);
        }
        return ans;
    }
}