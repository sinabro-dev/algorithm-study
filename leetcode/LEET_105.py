"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
"""
class Solution:
    """
    Keyword: Hash, Tree, Divide and Conquer
    Space: O(n)
    Time: O(n)
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder의 요소를 기준 노드로 삼고
        # inorder의 요소 중 기준 노드를 찾은 후,
        # 좌우로 나누어 child sub-tree를 재귀적으로 생성.

        inorder_map = dict()
        for idx, val in enumerate(inorder):
            inorder_map[val] = idx
        
        key_idx = 0

        def create(start: int, end: int) -> TreeNode:
            if start > end:
                return None
            
            nonlocal key_idx
            key_val = preorder[key_idx]
            key_idx += 1

            if start == end:
                return TreeNode(key_val)

            inorder_idx = inorder_map[key_val]

            left = create(start, inorder_idx-1)
            right = create(inorder_idx+1, end)

            node = TreeNode(key_val, left, right)
            return node
        
        tree = create(0, len(inorder)-1)
        return tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
