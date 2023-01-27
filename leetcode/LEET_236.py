"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    """
    Keyword: BFS, Tree
    Space: O(n)
    Time: O(n)
    """
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 먼저 `p`, `q` 두 노드를 동일한 level로 맞춘 후,
        # 하나씩 부모 노드로 올라가며 일치하는 지 확인하는 흐름.
        # 이를 위해서는 각 노드의 level과 부모 포인터가 필요.

        def bfs(node: TreeNode, level: int, parent: TreeNode):
            if not node:
                return

            node.level = level
            node.parent = parent

            bfs(node.left, level + 1, node)
            bfs(node.right, level + 1, node)

        bfs(root, 0, None)

        while p.level != q.level:
            if p.level < q.level:
                q = q.parent
            elif p.level > q.level:
                p = p.parent
        
        while p.val != q.val:
            p = p.parent
            q = q.parent
        
        return p
