"""
https://leetcode.com/problems/maximal-network-rank/description/

There is an infrastructure of n cities with some number of roads connecting these cities. Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.
The network rank of two different cities is defined as the total number of directly connected roads to either city. If a road is directly connected to both cities, it is only counted once.
The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.
Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.

Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
Output: 4
Explanation: The network rank of cities 0 and 1 is 4 as there are 4 roads that are connected to either 0 or 1. The road between 0 and 1 is only counted once.
"""
class Solution:
    """
    Keyword: Graph
    Space: O(e)
    Time: O(v^2)
    """
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # 각 노드마다 directly 연결된 간선의 수를 기록한 후
        # 모든 노드의 쌍을 조합하면서 directly 연결된 간선의 수를 구하는 방향
        # 이때 해당 노드의 쌍이 연결되어 있다면 중복 제거를 위해 간선의 수에서 -1을 함

        from collections import defaultdict

        mapper = defaultdict(int)
        conn = set()

        for a, b in roads:
            mapper[a] += 1
            mapper[b] += 1

            if a < b:
                conn.add((a, b))
            else:
                conn.add((b, a))
        
        ret = -1

        for i in range(n):
            for j in range(i+1, n):
                cur = mapper[i] + mapper[j]

                if (i, j) in conn:
                    cur -= 1
                
                ret = max(ret, cur)
        
        return ret
