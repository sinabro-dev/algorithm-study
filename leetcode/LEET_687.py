"""
https://leetcode.com/problems/longest-univalue-path/description/

Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.
The length of the path between two nodes is represented by the number of edges between them.

Input: root = [5,4,5,1,1,null,5]
Output: 2
Explanation: The shown image shows that the longest path of the same value (i.e. 5).
"""
class Solution:
    """
    Keyword: Tree, DFS, Diameter of Tree
    Space: O(n)
    Time: O(n)
    """
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        # DFS로 노드를 훑으며 각 경우에서의 `root`와 같은 `val`을 같는 경로의 최대 길이를 구하고,
        # 그 값이 지금까지의 값보다 크면 업데이트를 해주는 흐름.
        # 트리의 지름 (Diameter of tree) 알고리즘을 조금 변형한 것.

        max_len = 0

        def traverse(node: TreeNode) -> int:
            if not node:
                return 0
            
            nonlocal max_len
            left = node.left
            right = node.right
            
            left_len = traverse(left)
            right_len = traverse(right)

            if (left) and (left.val == node.val):
                left_len += 1
            else:
                left_len = 0
            
            if (right) and (right.val == node.val):
                right_len += 1
            else:
                right_len = 0
            
            max_len = max(max_len, left_len + right_len)
            return max(left_len, right_len)
        
        traverse(root)
        return max_len

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
