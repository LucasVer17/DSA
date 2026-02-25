class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        profit = 0
        right = 0
        while(right < len(prices)):
            final_price = prices[right] - prices[left]
            profit = max(profit, final_price)
            if prices[left] > prices[right]:
                left += 1
            else:
                right += 1
        return profit