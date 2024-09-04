class Solution {
    public int majorityElement(int[] nums) {
        int count = 0, ele = 0;
        for (int i : nums) {
            if (count == 0) {
                count++;
                ele = i;
            } else if (ele == i)
                count++;
            else
                count--;
        }
        return ele;
    }
}