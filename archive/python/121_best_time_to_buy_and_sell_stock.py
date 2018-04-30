# my solution (time exceed)
class Solution(object):

    def maxProfit(self, prices):
        max_profit = 0
        n_prices = len(prices)
        for index in range(n_prices):
            for sell in prices[index:]:
                profit = sell - prices[index]
                if profit > max_profit:
                    max_profit = profit
        return max_profit

# my solution 2(time exceed again)


class Solution(object):

    def maxProfit(self, prices):
        max_profit = 0
        n_prices = len(prices)
        for index in range(n_prices):
            profit = max(prices[index:]) - prices[index]
            if profit > max_profit:
                max_profit = profit
        return max_profit

# my solution3


class Solution(object):

    def maxProfit(self, prices):
        max_profit = 0
        if not prices:
            return 0
        min_price = prices[0]
        for price in prices:
            max_profit = max(max_profit, price - min_price)
            min_price = min(price, min_price)
            # print price, min_price, max_profit
        return max_profit
