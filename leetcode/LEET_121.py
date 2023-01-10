"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""
class Solution:
    """
    Keyword: Two Pointers
    Space: O(1)
    Time: O(N)
    """
    def maxProfit(self, prices: List[int]) -> int:
        # 처음에는 단순히 O(N^2) 흐름으로 접근해보았으나 시간 초과로, 개선이 필요.
        # 매수 금액의 최솟값을 업데이트해 가며 반복하여, 수익이 더 큰 경우를 찾아내는 흐름.

        min_day = 0
        max_profit = 0

        for cur_day in range(1, len(prices)):
            if prices[cur_day] < prices[min_day]:
                min_day = cur_day
            
            cur_profit = prices[cur_day] - prices[min_day]
            max_profit = max(cur_profit, max_profit)
        
        return max_profit
