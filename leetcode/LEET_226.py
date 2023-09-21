"""
https://leetcode.com/problems/invert-binary-tree/description/

Given the root of a binary tree, invert the tree, and return its root.
- The number of nodes in the tree is in the range [0, 100].
- 100 <= Node.val <= 100

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
"""
class Solution:
    """
    Keyword: DFS, Binary Tree
    Space: O(n)
    Time: O(n)
    """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def do(node: TreeNode) -> None:
            if not node:
                return
            
            do(node.left)
            do(node.right)

            tmp = node.left
            node.left = node.right
            node.right = tmp
        
        do(root)
        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
