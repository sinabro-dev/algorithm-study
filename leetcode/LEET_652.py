"""
https://leetcode.com/problems/find-duplicate-subtrees/description/

Given the root of a binary tree, return all duplicate subtrees.
For each kind of duplicate subtrees, you only need to return the root node of any one of them.
Two trees are duplicate if they have the same structure with the same node values.

Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]
"""
class Solution:
    """
    Keyword: Hash, DFS, Tree
    Space: O(n)
    Time: O(n)
    """
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # DFS로 트리의 모든 노드를 훑으며,
        # 각 서브 트리를 문자열로 표현하여 해시값 비교를 통해 존재여부를 확인
        # 이때 문자열 표현 시, 노드의 값을 이용하되 항상 양수가 되도록 +201을 하여 표현
        # 또한 left 또는 right가 없는 경우에는 '000'으로 표현하여 구분

        from collections import defaultdict

        offset = 201
        mapper = dict()
        counter = defaultdict(int)

        def traverse(node: TreeNode) -> str:
            if node == None:
                return '000'

            parent = str(node.val + offset)
            left = traverse(node.left)
            right = traverse(node.right)

            expr = ''.join([parent, left, right])
            mapper[expr] = node
            counter[expr] += 1

            return expr
        
        traverse(root)

        subtrees = list()
        for expr, count in counter.items():
            if count <= 1:
                continue

            subtrees.append(mapper[expr])
        
        return subtrees


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
