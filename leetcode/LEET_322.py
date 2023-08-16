"""
https://leetcode.com/problems/coin-change/description/

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
"""
class Solution:
    """
    Keyword: Dynamic Programming
    Space: O(amount)
    Time: O(n * amount)
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp(i) = 1 + min( dp(i - coin_1), dp(i - coin_2), ..., dp(i - coin_n) )

        memo = [-1 for _ in range(amount+1)]
        for coin in coins:
            if coin > amount:
                continue
            memo[coin] = 1
        memo[0] = 0

        for i in range(1, amount+1):
            if memo[i] != -1:
                continue

            can_made = False
            val = 10**4

            for coin in coins:
                if i < coin:
                    continue
                
                if memo[i - coin] == -1:
                    continue
                
                can_made = True
                val = min(val, memo[i - coin])
            
            if can_made:
                memo[i] = val + 1
            else:
                memo[i] = -1
        
        return memo[amount]
