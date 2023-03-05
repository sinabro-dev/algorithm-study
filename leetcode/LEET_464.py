"""
https://leetcode.com/problems/can-i-win/description/

In the "100 game" two players take turns adding, to a running total, any integer from 1 to 10. The player who first causes the running total to reach or exceed 100 wins.
What if we change the game so that players cannot re-use integers?
For example, two players might take turns drawing from a common pool of numbers from 1 to 15 without replacement until they reach a total >= 100.
Given two integers maxChoosableInteger and desiredTotal, return true if the first player to move can force a win, otherwise, return false. Assume both players play optimally.

Input: maxChoosableInteger = 10, desiredTotal = 11
Output: false
Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.
"""
class Solution:
    """
    Keyword: DP, Memoization
    Space: O(n)
    Time: O(n^2)
    """
    def canIWin(self, max_choosable: int, desired_total: int) -> bool:
        # `desired_total` <= `max_choosable`이면 언제나 True
        # `desired_total` > sum of [1, `max_choosable`]이면 언제나 False
        # 이외의 경우들은 1부터 `desired_total`까지 훑으며 해당 숫자일 때
        # 게임의 승자는 누구인가를 구하고, 그 과정에서 메모이제이션을 활용.

        if desired_total > max_choosable*(max_choosable+1)/2:
            return False
        if desired_total <= max_choosable:
            return True

        @cache
        def memoize(nums: frozenset, total: int) -> bool:
            if total <= 0:
                return False
            
            for num in nums:
                prev = memoize(nums-{num}, total-num)
                if prev == False:
                    return True
            
            return False
        
        nums = frozenset(list(range(1, max_choosable+1)))
        return memoize(nums, desired_total)
