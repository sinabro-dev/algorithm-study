"""
https://leetcode.com/problems/recover-binary-search-tree/description/

You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
"""
class Solution:
    """
    Kewyord: DFS, BST, In-Order Traversal
    Space: O(n)
    Time: O(n)
    """
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        # 중위 순회하며 크기 비교

        prev, start, last = None, None, None

        def traverse(node: TreeNode) -> None:
            if not node:
                return
            
            traverse(node.left)

            nonlocal prev, start, last
            if prev and prev.val > node.val:
                if not start:
                    start = prev
                last = node
            
            prev = node

            traverse(node.right)
        
        traverse(root)

        if start and last:
            start.val, last.val = last.val, start.val

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
