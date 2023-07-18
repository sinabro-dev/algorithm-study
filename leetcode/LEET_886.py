"""
https://leetcode.com/problems/possible-bipartition/description/

We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.
Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.

Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Explanation: We need at least 3 groups to divide them. We cannot put them in two groups.
"""
class Solution:
    """
    Keyword: Union Find
    Space: O(n)
    Time: O(n)
    """
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        padding = n+1
        parents = [i for i in range(2*padding)]

        def find(child: int) -> int:
            if child == parents[child]:
                return child
            parents[child] = find(parents[child])
            return parents[child]
        
        def union(child1: int, child2: int):
            parent1, parent2 = find(child1), find(child2)
            if parent1 == parent2:
                return
            parents[parent2] = parent1

        for [a, b] in dislikes:
            union(a, b + padding)
            union(a + padding, b)
        
        for i in range(1, padding):
            if find(i) == find(i + padding):
                return False
        return True
