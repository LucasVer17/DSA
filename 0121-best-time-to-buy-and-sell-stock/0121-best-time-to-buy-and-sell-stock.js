/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let left = 0
    let right = 1
    let profit = 0
    while(right < prices.length)
    {
        finalPrice = prices[right] - prices[left]
        profit = Math.max(profit, finalPrice)
        if(prices[right] < prices[left])
        {
            left++
        }
        else
        {
            right++
        }
    }

    return profit
};