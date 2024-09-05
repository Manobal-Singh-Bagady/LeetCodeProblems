class Solution {
    public int subarraySum(int[] nums, int k) {
        Map<Integer, Integer> hash = new HashMap<>();
        int sum = 0;
        int count = 0;
        for(int i = 0; i<nums.length; i++){
            sum+=nums[i];
            if(sum==k) count++;
            count += hash.getOrDefault(sum-k, 0);
            hash.put(sum, hash.getOrDefault(sum, 0)+1);
        }
        return count;
    }
}