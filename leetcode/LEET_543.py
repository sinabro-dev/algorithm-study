"""
https://leetcode.com/problems/diameter-of-binary-tree/description/

Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Keyword: Tree, DFS
    Space: O(N)
    Time: O(N)
    """
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # DFS를 2번 수행하며, 트리의 지름을 구하는 흐름.
        # 첫번째 DFS는 가장 깊은 노드를 찾기 위함이고,
        # 두번째 DFS는 가장 깊은 노드에서 가장 먼 노드를 찾기 위함임.

        from collections import deque

        def setup_parent(root: TreeNode):
            stack = deque()
            root.parent = None
            stack.append(root)

            while stack:
                node = stack.pop()

                for child in [node.right, node.left]:
                    if not child:
                        continue
                    
                    child.parent = node
                    stack.append(child)
            
            return root

        def dfs_farthest(start: TreeNode) -> (TreeNode, int):
            deep_node = start
            deep_distance = 0

            stack = deque()
            stack.append((None, start, 0))

            while stack:
                (prev_node, cur_node, cur_distance) = stack.pop()

                for next_node in [cur_node.parent, cur_node.left, cur_node.right]:
                    if not next_node:
                        continue
                    if next_node == prev_node:
                        continue
                    
                    stack.append((cur_node, next_node, cur_distance+1))
                
                if cur_distance > deep_distance:
                    deep_distance = cur_distance
                    deep_node = cur_node
            
            return (deep_node, deep_distance)
        
        setup_parent(root)
        (farthest_node, _) = dfs_farthest(root)
        (_, diameter) = dfs_farthest(farthest_node)
        return diameter
