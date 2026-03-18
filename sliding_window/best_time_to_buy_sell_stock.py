# Pattern: Sliding Window — track minimum buy price, maximize profit at each sell point
# Trigger: "max profit" = one pass = track best buy seen so far + check profit at each price

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]
        for sell in prices:
            maxP = max(maxP, sell - minBuy)  # profit if we sell today
            minBuy = min(minBuy, sell)        # update cheapest buy price seen so far
        return maxP
    