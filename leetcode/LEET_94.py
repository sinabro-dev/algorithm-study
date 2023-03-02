"""
https://leetcode.com/problems/binary-tree-inorder-traversal/description/

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Input: root = [1,null,2,3]
Output: [1,3,2]
"""
class Solution:
    """
    Keyword: Tree, DFS, Stack
    Space: O(n)
    Time: O(n)
    """
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = list()
        stack = list()
        ptr = root
        
        while True:
            while ptr != None:
                stack.append(ptr)
                ptr = ptr.left
            
            if not stack:
                break
            
            ptr = stack.pop()
            ret.append(ptr.val)
            ptr = ptr.right

        return ret
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
