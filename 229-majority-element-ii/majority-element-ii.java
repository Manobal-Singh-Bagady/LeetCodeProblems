class Solution {
    public List<Integer> majorityElement(int[] nums) {
        int count1 = 0, count2 = 0, ele1 = 0, ele2 = 0;
        for (int i : nums) {
            if (count1 == 0 && i != ele2) {
                count1++;
                ele1 = i;
            } else if (count2 == 0 && i != ele1) {
                count2++;
                ele2 = i;
            } else if (i == ele1)
                count1++;
            else if (i == ele2)
                count2++;
            else {
                count1--;
                count2--;
            }
        }

        List<Integer> ans = new ArrayList<>();
        count1 = 0;
        count2 = 0;
        for (int i : nums) {
            if (i == ele1)
                count1++;
            if (i == ele2)
                count2++;
        }
        if (count1 > nums.length / 3)
            ans.add(ele1);
        if (count2 > nums.length / 3 && ele2!=ele1)
            ans.add(ele2);
        return ans;
    }
}