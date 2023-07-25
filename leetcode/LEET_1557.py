"""
https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/description/

Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.
Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.
Notice that you can return the vertices in any order.

Input: n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
Output: [0,3]
Explanation: It's not possible to reach all the nodes from a single vertex. From 0 we can reach [0,1,2,5]. From 3 we can reach [3,4,2,5]. So we output [0,3].
"""
class Solution:
    """
    Keyword: Graph
    Space: O(e)
    Time: O(v)
    """
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # incoming edge가 없는 노드의 경우 반드시 반환하고자 하는 집합에 포함되어야 함
        # incoming edge가 있는 노드의 경우 어떻게서든지 다른 노드로부터 접근할 수 있음

        incomings = collections.defaultdict(set)

        for edge in edges:
            incomings[edge[1]].add(edge[0])
        
        ret = list()
        for node in range(n):
            if len(incomings[node]) == 0:
                ret.append(node)

        return ret
