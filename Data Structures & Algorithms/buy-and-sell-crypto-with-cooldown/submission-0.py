class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} 

        def dfs(i, canBuy):
            if i >= len(prices):
                return 0
            if (i, canBuy) in dp:
                return dp[(i, canBuy)]
            
            if canBuy: # u can either buy or keep
                buy = dfs(i + 1, False) - prices[i] # False bcoz u cant buy if u bought once
                hold = dfs(i + 1, True)
                dp[(i, canBuy)] = max(buy, hold) # take which gave max returns
            else: # if u cant buy then u have to hold or sell
                sell = dfs(i + 2, True) + prices[i]
                hold = dfs(i + 1, False)
                dp[(i, canBuy)] = max(sell, hold)
            
            return dp[(i, canBuy)]
        
        return dfs(0, True)