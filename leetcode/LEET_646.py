"""
https://leetcode.com/problems/maximum-length-of-pair-chain/description/

You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.
A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.
Return the length longest chain which can be formed.
You do not need to use up all the given intervals. You can select pairs in any order.

Input: pairs = [[1,2],[7,8],[4,5]]
Output: 3
Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].
"""
class Solution:
    """
    Keyword: Dynamic Programming, Sort
    Space: O(n)
    Time: O(nlogn)
    """
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # pairs를 오름차순으로 정렬 후
        # 특정 구간까지의 최대 chain 길이를 memo 해둠

        pairs.sort(key=lambda x : (x[1], x[0]))
        n = len(pairs)
        first, last = 1000, -1000
        for left, right in pairs:
            first = min(first, left)
            last = max(last, right)

        memo = dict()
        for k in range(first-1, last+1):
            memo.update({k: -1})
        memo.update({first-1: 0})
        
        idx = 0
        for cur in range(first, last+1):
            while idx < n and pairs[idx][1] == cur:
                left, right = pairs[idx][0], pairs[idx][1]
                memo.update({right: max(memo.get(right-1), memo.get(left-1) + 1)})
                idx += 1
            
            if memo.get(cur) == -1:
                memo.update({cur: memo.get(cur-1)})
        
        return memo.get(last)
