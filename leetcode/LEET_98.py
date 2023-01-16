"""
https://leetcode.com/problems/validate-binary-search-tree/description/

Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Keyword: DFS, BST
    Space: O(N)
    Time: O(N)
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # In-order 순회하는 흐름으로 접근.

        def traversal(node: TreeNode) -> (bool, int, int):
            val = node.val
            left_child = node.left
            right_child = node.right
            
            left_from = val
            if left_child:
                (valid, left_from, left_to) = traversal(left_child)
                if (not valid) or (not left_to < val):
                    return (False, 0, 0)
            
            right_to = val
            if right_child:
                (valid, right_from, right_to) = traversal(right_child)
                if (not valid) or (not val < right_from):
                    return (False, 0, 0)
            
            return (True, left_from, right_to)

        (valid, _, _) = traversal(root)
        return valid
