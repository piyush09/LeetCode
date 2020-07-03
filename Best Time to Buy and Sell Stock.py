"""
Algo: Maintain two variables minimum price and maximum profit while iterating through the prices list once.
      Update max profit by (current price - min. price) if there is a better obtained value.
T.C. - O(N), as only iterating through the prices list once, 'N' number of items in prices list.
S.C - O(1) - Only space is required for max_profit and min_price variables.
"""

def maxProfit(prices):
    max_profit = 0
    min_price = float('inf')

    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)

    return max_profit

prices = [7,1,5,3,6,4]
print (maxProfit(prices))