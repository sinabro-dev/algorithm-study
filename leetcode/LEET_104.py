"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Input: root = [3,9,20,null,null,15,7]
Output: 3
"""
class Solution:
    """
    Keyword: DFS, BFS, Tree
    Space: O(n)
    Time: O(n)
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0

        def traverse(node: TreeNode, depth: int) -> None:
            nonlocal max_depth

            if not node:
                max_depth = max(max_depth, depth - 1)
                return
            
            traverse(node.left, depth+1)
            traverse(node.right, depth+1)
        
        traverse(root, 1)
        return max_depth
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
