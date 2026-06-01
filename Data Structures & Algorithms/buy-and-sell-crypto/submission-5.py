class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #main indea is buy at low and sell at high

        left = 0
        MaxProfit = 0

        for right in range(1,len(prices)):
            if prices[left]>prices[right]:
                left = right
            else:
                MaxProfit = max(MaxProfit, prices[right] - prices[left])

        return MaxProfit