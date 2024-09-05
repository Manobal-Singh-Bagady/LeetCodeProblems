class Solution {
    public List<Integer> majorityElement(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i : nums)
            map.put(i, map.getOrDefault(i, 0) + 1);

        List<Integer> ans = new ArrayList<>();
        int n = nums.length;
        for(Map.Entry<Integer, Integer> e: map.entrySet()){
            if(e.getValue()>n/3)ans.add(e.getKey());
        }
        return ans;
    }
}