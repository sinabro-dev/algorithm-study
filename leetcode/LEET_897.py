"""
https://leetcode.com/problems/increasing-order-search-tree/description/

Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
"""
class Solution:
    """
    Keyword: Binary Search Tree (BST), Stack, In-Order Traversal
    Space: O(n)
    Time: O(n)
    """
    def increasingBST(self, root: TreeNode) -> TreeNode:
        head = None
        check, ptr = root, root
        stack = list()

        while check or stack:
            if check:
                stack.append(check)
                check = check.left
                continue
            
            node = stack.pop()
            node.left = None
            check = node.right

            if not head:
                head = node
                ptr = node
                continue
            
            ptr.right = node
            ptr = node
        
        return head


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
