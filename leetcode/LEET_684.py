"""
https://leetcode.com/problems/redundant-connection/description/

In this problem, a tree is an undirected graph that is connected and has no cycles.
You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.
Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
"""
class Solution:
    """
    Keyword: Union Find, DFS
    Space: O(n)
    Time: O(n)
    """
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # union-find 알고리즘을 이용해, 추가되는 간선이 이미 존재하는 두 집합을 잇는 경우를 탐지.

        parents = [node for node in range(len(edges)+1)]

        def find(node: int) -> int:
            if node == parents[node]:
                return node
            
            return find(parents[node])
        
        def union(node1: int, node2: int):
            parent1, parent2 = find(node1), find(node2)

            if parent1 == parent2:
                return
            
            parents[parent2] = parent1
        
        for edge in edges:
            src, dst = edge[0], edge[1]

            if find(src) == find(dst):
                return edge
            
            union(src, dst)
        
        return list()
