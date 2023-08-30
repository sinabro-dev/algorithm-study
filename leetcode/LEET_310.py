"""
https://leetcode.com/problems/minimum-height-trees/description/

A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.
Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).
Return a list of all MHTs' root labels. You can return the answer in any order.
The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
- 1 <= n <= 2 * 104
- edges.length == n - 1
- 0 <= ai, bi < n
- ai != bi
- All the pairs (ai, bi) are distinct.
- The given input is guaranteed to be a tree and there will be no repeated edges

Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
"""
class Solution:
    """
    Keyword: Topological Sort, BFS, DFS
    Space: O(e)
    Time: O(v)
    """
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # 모든 leaf 노드에서 pointer를 두어 각각 traverse 시작하여 인접 노드로 하나씩 upward 이동
        # 특정 노드에서 pointer가 만나는 경우 하나의 pointer만 유지하며 반복 수행
        # 아직 훑지 않은 노드의 수가 2 이하가 될 때 문제에서 원하는 최소 높이를 구한 것

        if n == 1:
            return [0]

        adj = [list() for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        leaves = list()
        for node in range(n):
            if len(adj[node]) == 1:
                leaves.append(node)
        
        while n > 2:
            n -= len(leaves)
            
            new_leaves = list()
            for leaf in leaves:
                parent = adj[leaf].pop()
                adj[parent].remove(leaf)

                if len(adj[parent]) == 1:
                    new_leaves.append(parent)
            
            leaves = new_leaves
        
        return leaves
