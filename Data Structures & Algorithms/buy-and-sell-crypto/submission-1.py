class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for idx, price in enumerate(prices):

            if max(prices[idx:]) > price:
                if max(prices[idx:]) - price > profit:
                    profit = max(prices[idx:]) - price

            # if idx == 0 or idx + 1 == len(prices): continue

            # if prices[idx-1] > price:
            #     maxprice = max(prices[idx+1:])
            #     if maxprice - price > profit:
            #         profit = maxprice - price
        return profit