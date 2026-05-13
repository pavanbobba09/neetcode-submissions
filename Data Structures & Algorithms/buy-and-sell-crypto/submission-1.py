class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left = 0
        right = 1
        profit = 0

        while right <len(prices):
            if prices[left]<prices[right]:
                value = prices[right]-prices[left]
                profit = max(value,profit)

            else:
                left = right

            right+=1

        return profit
        

        #2 pointer idea is mine how the code is from gpt