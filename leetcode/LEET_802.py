"""
https://leetcode.com/problems/find-eventual-safe-states/description/

There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].
A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).
Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Explanation: The given graph is shown above.
Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.
"""
class Solution:
    """
    Keyword: Topological Sort
    Space: O(n)
    Time: O(n)
    """
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # 노드들을 훑으며 해당 노드와 연결된 노드가 safe / terminal 노드인지 확인하여 판단한다
        # 이때 연결된 노드가 아직 판단되지 않았다면 재귀적으로 다시 다음 연결된 노드를 확인한다
        # 그 과정에서 그래프 루프를 탐지하여 재귀 중단을 할 수 있도록 탐색 정보를 기록하며 진행한다

        safes = dict()
        safes = [0 for _ in range(len(graph))]
        
        def validate(node: int) -> bool:
            if safes[node] != 0:
                return
            
            safes[node] = 1

            for conn in graph[node]:
                if safes[conn] == 1:
                    return False

                if safes[conn] == 2:
                    continue
                
                if not validate(conn):
                    return
            
            safes[node] = 2
            return True
        
        ret = list()
        for node in range(len(graph)):
            validate(node)

            if safes[node] == 2:
                ret.append(node)
        
        return ret
