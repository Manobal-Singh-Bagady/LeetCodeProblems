class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> hash = new HashMap<>();
        for (int i : nums) {
            hash.put(i, hash.getOrDefault(i, 0) + 1);
        }
        return Collections.max(hash.entrySet(), Map.Entry.comparingByValue()).getKey();

        // AtomicInteger ans = new AtomicInteger();
        // hash.entrySet().forEach(e -> {
        //     if (e.getValue() > nums.length / 2)
        //         ans.set(e.getKey());
        // });
        // return ans.get();
    }
}