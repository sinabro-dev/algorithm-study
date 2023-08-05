"""
https://leetcode.com/problems/unique-binary-search-trees-ii/description/

Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
"""
class Solution:
    """
    Keyword: Backtracking, Binary Search
    Space: O(2^n)
    Time: O(2^n)
    """
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate(left, right: int) -> List[Optional[TreeNode]]:
            if left == right:
                return [None]
            
            nodes = list()

            for num in range(left, right):
                for left_child in generate(left, num):
                    for right_child in generate(num+1, right):
                        node = TreeNode(num+1)
                        node.left = left_child
                        node.right = right_child
                        nodes.append(node)
            
            return nodes
        
        return generate(0, n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
