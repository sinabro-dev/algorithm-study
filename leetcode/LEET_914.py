"""
https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/description/

You are given an integer array deck where deck[i] represents the number written on the ith card.
Partition the cards into one or more groups such that:
- Each group has exactly x cards where x > 1, and
- All the cards in one group have the same integer written on them.
Return true if such partition is possible, or false otherwise.

Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
"""
class Solution:
    """
    Keyword: Hash, Number Theory (GCD)
    Space: O(n)
    Time: O(n)
    """
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from collections import defaultdict

        cnt_map = defaultdict(int)
        for card in deck:
            cnt_map[card] += 1
        
        def gcd(a: int, b: int) -> int:
            if a < b:
                a, b = b, a
            
            while b != 0:
                tmp = a % b
                a = b
                b = tmp
            
            return a
        
        group_size = cnt_map[deck[0]]
        for cnt in cnt_map.values():
            group_size = gcd(cnt, group_size)
        
        if group_size < 2:
            return False
        
        for cnt in cnt_map.values():
            if cnt % group_size != 0:
                return False
        
        return True
