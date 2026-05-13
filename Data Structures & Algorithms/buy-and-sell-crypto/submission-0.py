class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i]<prices[j]:
                    value = prices[j]-prices[i]
                    profit = max(profit,value)

        return profit

    #this is an brute force approch