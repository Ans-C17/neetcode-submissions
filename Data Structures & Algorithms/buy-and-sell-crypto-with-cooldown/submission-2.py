class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} # idx, amt -> maxProf

        def dfs(i, canBuy):
            if i >= len(prices):
                return 0

            if (i, canBuy) in dp:
                return dp[(i, canBuy)]

            if canBuy:
                buy = dfs(i + 1, False) - prices[i]
                wait = dfs(i + 1, True)
                maxProf = max(buy, wait)
            else:
                sell = dfs(i + 2, True) + prices[i]
                wait = dfs(i + 1, False)
                maxProf = max(sell, wait)

            dp[(i, canBuy)] = maxProf
            return dp[(i, canBuy)]
        
        return dfs(0, True)
            