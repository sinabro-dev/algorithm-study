"""
https://leetcode.com/problems/same-tree/description/

Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Input: p = [1,2,1], q = [1,1,2]
Output: false
"""
class Solution:
    """
    Keyword: Tree, BFS
    Space: O(n+m)
    Time: O(n+m)
    """
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p == None) and (q == None):
            return True
        if (p == None) and (q != None):
            return False
        if (p != None) and (q == None):
            return False

        from collections import deque

        queue_p, queue_q = deque(), deque()
        queue_p.append(p)
        queue_q.append(q)

        while queue_p and queue_q:
            node_p, node_q = queue_p.pop(), queue_q.pop()

            if node_p.val != node_q.val:
                return False
            
            if (node_p.left == None) != (node_q.left == None):
                return False
            if node_p.left:
                queue_p.append(node_p.left)
                queue_q.append(node_q.left)
            
            if (node_p.right == None) != (node_q.right == None):
                return False
            if node_p.right:
                queue_p.append(node_p.right)
                queue_q.append(node_q.right)
        
        if queue_p:
            return False
        if queue_q:
            return False

        return True
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
