"""
https://leetcode.com/problems/binary-tree-level-order-traversal/description/

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Keyword: BFS
    Space: O(n)
    Time: O(n)
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = list()

        if not root:
            return ret

        from collections import deque

        deq = deque()
        deq.append((0, root))

        while deq:
            level, node = deq.popleft()

            if level > len(ret) - 1:
                ret.append([node.val])
            else:
                ret[level].append(node.val)
            
            if node.left:
                deq.append((level + 1, node.left))
            if node.right:
                deq.append((level + 1, node.right))
        
        return ret
