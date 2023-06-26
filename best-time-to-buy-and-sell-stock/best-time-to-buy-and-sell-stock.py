class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        maxProfit = 0
        for x in prices[1:]:
            maxProfit = max(maxProfit, x-mini)
            mini = min(mini,x)
        return maxProfit

