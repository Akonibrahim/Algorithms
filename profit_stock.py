# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Time exceeded
# class Solution: 
#     def maxProfit(self, prices) -> int:
#         output = 0
#         for i in range(len(prices)):
#             for j in range(len(prices)):
#                 if i != j and j > i:
#                     profit = prices[j] - prices[i]
#                     if profit > output:
#                         output = profit
#         return output

# Time exceeded
# class Solution:
#     def maxProfit(self, prices) -> int:
#         output = 0
#         for i in range(len(prices)):
#             subset = prices[i+1:]
#             if subset:
#                 profit = max(subset) - prices[i]
#                 if profit > output:
#                     output = profit
#         return output


class Solution:
    def maxProfit(self, prices) -> int:
        left, right = 0, 1
        maxProfit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(profit, maxProfit)
            else:
                left = right
            right += 1
        return maxProfit

prices = [7,1,5,3,6,4]
s = Solution()
print(s.maxProfit(prices))