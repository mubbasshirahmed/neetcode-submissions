class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_profit = 0
        max_profit = 0 
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                curr_profit = prices[j] - prices[i]

                max_profit = max(curr_profit, max_profit)

        return max_profit  

            


