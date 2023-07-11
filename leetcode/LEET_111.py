"""
https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.

Input: root = [3,9,20,null,null,15,7]
Output: 2
"""
class Solution:
    """
    Keyword: BFS, Binary Tree
    Space: O(n)
    Time: O(n)
    """
    def minDepth(self, root: Optional[TreeNode]) -> int:
        from collections import deque

        if not root:
            return 0

        queue = deque()
        queue.append((root, 1))

        while queue:
            cur, cnt = queue.popleft()

            if not cur.left and not cur.right:
                return cnt

            if cur.left:
                queue.append((cur.left, cnt+1))
            if cur.right:
                queue.append((cur.right, cnt+1))


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
