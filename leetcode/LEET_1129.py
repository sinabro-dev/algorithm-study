"""
https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:
- redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
- blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.

Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
Output: [0,1,-1]
"""
class Solution:
    """
    Keyword: BFS
    Space: O(v * e)
    Time: O(e)
    """
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        graph = [[list(), list()]for _ in range(n)]

        for src, dst in red_edges:
            graph[src][0].append(dst)

        for src, dst in blue_edges:
            graph[src][1].append(dst)
        
        paths = [[2*n, 2*n] for _ in range(n)]
        paths[0] = [0, 0]

        queue = [[0, 0], [0, 1]]

        for src, color in queue:
            for dst in graph[src][color]:
                if paths[dst][color] != 2*n:
                    continue
                paths[dst][color] = 1 + paths[src][1-color]
                queue.append([dst, 1-color])
        
        answers = list()

        for red_val, blue_val in paths:
            val = min(red_val, blue_val)
            if val == 2*n:
                answers.append(-1)
            else:
                answers.append(val)
        
        return answers
