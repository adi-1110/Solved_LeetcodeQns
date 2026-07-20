class Solution(object):
    def maxProfit(self, prices):
        l=prices[0]
        max_profit=0

        for price in prices:
            l=min(l,price)
            profit= price - l
            max_profit=max(max_profit,profit)
        return max_profit
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna