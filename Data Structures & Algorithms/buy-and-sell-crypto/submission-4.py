class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        profit = 0

        for right in range(1,len(prices)):
            if prices[left]>prices[right]:
                #here we have an high lets move to the next one
                left = right
            else:
                profit = max(profit, prices[right]-prices[left])


        return profit
        