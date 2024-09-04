class Solution {
    public int missingNumber(int[] nums) {
        int[] hash = new int[nums.length + 1];
        for (int i : nums)
            hash[i]++;
        for (int i = 0; i < hash.length; i++) {
            if (hash[i] == 0)
                return i;
        }
        return -1;
    }
}