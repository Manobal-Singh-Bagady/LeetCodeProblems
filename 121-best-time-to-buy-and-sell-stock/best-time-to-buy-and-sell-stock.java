class Solution {
    public int maxProfit(int[] prices) {
        int min = prices[0], ans = 0;
        for(int i: prices){
            ans = Math.max(ans, i-min);
            min = Math.min(min, i);
        }
        return ans;
    }
}