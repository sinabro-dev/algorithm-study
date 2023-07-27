"""
https://leetcode.com/problems/find-the-town-judge/description/

In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
If the town judge exists, then:
1. The town judge trusts nobody.
2. Everybody (except for the town judge) trusts the town judge.
3. There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.
Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
"""
class Solution:
    """
    Keyword: Hash Table
    Space: O(n)
    Time: O(n)
    """
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # trust 요소를 훑으며 각 사람마다 자신이 믿는 사람과 믿고 있는 사람의 수를 카운트한 후
        # 믿는 사람이 0명이고 믿고 있는 사람이 n-1명인 사람이 존재하는 지 확인

        info = [[0, 0] for _ in range(n+1)]

        for src, dst in trust:
            info[src][0] += 1
            info[dst][1] += 1
        
        for i in range(1, n+1):
            [believer, believed] = info[i]
            if believer == 0 and believed == n-1:
                return i
        
        return -1
