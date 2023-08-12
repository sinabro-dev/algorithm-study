"""
https://leetcode.com/problems/coin-change-ii/description/

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.
You may assume that you have an infinite number of each kind of coin.
The answer is guaranteed to fit into a signed 32-bit integer.

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
"""
class Solution:
    """
    Keyword: Dynamic Programming
    Space: O(amount)
    Time: O(amount * len(coins))
    """
    def change(self, amount: int, coins: List[int]) -> int:
        # dp(i) += dp(i - coin_value)
        # [Case] coins: [1,2,5], amount: 5
        # 1) init
        # memo = [1, 0, 0, 0, 0, 0]
        # 2) process coin[0]
        # memo[i] += memo[i - 1]
        # memo => [1, 1, 1, 1, 1, 1]
        # 3) process coin[1]
        # memo[i] += memo[i - 2]
        # memo => [1, 1, 2, 2, 3, 3]
        # 4) process coin[2]
        # memo[i] += memo[i - 5]
        # memo => [1, 1, 2, 2, 3, 4]

        memo = [0 for _ in range(amount+1)]
        memo[0] = 1
        
        for coin in coins:
            for i in range(coin, amount+1):
                memo[i] += memo[i - coin]
        
        return memo[amount]
