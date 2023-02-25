"""
https://leetcode.com/problems/all-paths-from-source-to-target/description/

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.
The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
"""
class Solution:
    """
    Keyword: Backtracking, DFS
    Space: O(n)
    Time: O(n)
    """
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # DFS로 이전에 방문한 적 없는 정점을 훑으며 목적지에 도달하는지 확인

        paths = list()

        stack = list()
        stack.append((0, [0]))

        while stack:
            node, path = stack.pop()

            if node == len(graph)-1:
                paths.append(path)
                continue
            
            for adj in graph[node]:
                stack.append((adj, path+[adj]))
        
        return paths
