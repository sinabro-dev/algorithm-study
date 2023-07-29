"""
https://leetcode.com/problems/predict-the-winner/description/

You are given an integer array nums. Two players are playing a game with this array: player 1 and player 2.
Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of 0. At each turn, the player takes one of the numbers from either end of the array (i.e., nums[0] or nums[nums.length - 1]) which reduces the size of the array by 1. The player adds the chosen number to their score. The game ends when there are no more elements in the array.
Return true if Player 1 can win the game. If the scores of both players are equal, then player 1 is still the winner, and you should also return true. You may assume that both players are playing optimally.

Input: nums = [1,5,233,7]
Output: true
Explanation: Player 1 first chooses 1. Then player 2 has to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.
"""
class Solution:
    """
    Keyword: Recursion, Game Theory, Minimax
    Space: O(n^2)
    Time: O(n^2)
    """
    def PredictTheWinner(self, nums: List[int]) -> bool:
        # Minimax 알고리즘을 이용해 풀이

        def minimax(start, end: int) -> int:
            if start == end:
                return nums[start]
            
            val1 = nums[start] - minimax(start+1, end)
            val2 = nums[end] - minimax(start, end-1)
            return max(val1, val2)
        
        score = minimax(0, len(nums)-1)
        if score >= 0:
            return True
        else:
            return False
