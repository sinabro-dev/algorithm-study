"""
https://leetcode.com/problems/balanced-binary-tree/description/

Given a binary tree, determine if it is height-balanced.

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
"""
class Solution:
    """
    Keyword: DFS
    Space: O(n)
    Time: O(n)
    """
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def check(node: TreeNode) -> (bool, int):
            if not node.left and not node.right:
                return (True, 1)
            
            left_status, left_depth = True, 0
            if node.left:
                left_status, left_depth = check(node.left)

            right_status, right_depth = True, 0
            if node.right:
                right_status, right_depth = check(node.right)

            if not (left_status & right_status):
                return (False, 0)

            if abs(left_depth - right_depth) > 1:
                return (False, 0)

            depth = max(left_depth, right_depth) + 1
            return (True, depth)

        status, _ = check(root)
        return status


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
