"""
https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any non-empty path.

Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
"""
class Solution:
    """
    Keyword: DP(Dynamic Programming), DFS, Binary Tree, Recursion
    Space: O(n)
    Time: O(n)
    """
    def maxPathSum(self, root: TreeNode) -> int:
        # https://leetcode.com/problems/binary-tree-maximum-path-sum/solutions/603423/python-recursion-stack-thinking-process-diagram/

        max_gain = -1001
        
        def get_gain(node: TreeNode) -> int:
            if node is None:
                return 0
            
            nonlocal max_gain

            left_gain = max(get_gain(node.left), 0)
            right_gain = max(get_gain(node.right), 0)

            cur_gain = node.val + left_gain + right_gain
            max_gain = max(max_gain, cur_gain)

            return node.val + max(left_gain, right_gain)

        get_gain(root)
        return max_gain
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
