"""
https://leetcode.com/problems/all-possible-full-binary-trees/description/

Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.
Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.
A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Input: n = 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
"""
class Solution:
    """
    Keyword: Recursion, Memoization
    Space: O(n)
    Time: O(2^n)
    """
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # 재귀적으로 왼쪽에 i개 만큼 노드를 만들면 오른쪽에는 n-i-1개 만큼 노드를 만들어야 함
        # 이를 반복 호출해서 FBT 생성하는데, 같은 구조의 FBT 중복 생성을 방지하기 위해
        # 메모이제이션도 함께 활용

        if n % 2 == 0:
            return list()

        memo = dict()
        
        def build(k: int) -> list:
            if k in memo:
                return memo[k]
            
            if k == 1:
                memo[k] = [TreeNode(0)]
                return memo[k]
            
            tree = list()

            for i in range(1, k-1, 2):
                lefts = build(i)
                rights = build(k-i-1)

                for left in lefts:
                    for right in rights:
                        tree.append(TreeNode(0, left, right))
            
            memo[k] = tree
            return memo[k]

        return build(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
