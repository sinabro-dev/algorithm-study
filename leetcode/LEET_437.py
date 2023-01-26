"""
https://leetcode.com/problems/path-sum-iii/description/

Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Keyword: DFS, Hash Map
    Space:O(n)
    Time: O(n)
    """
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # 항상 downwards로 합을 구해야 하므로, DFS 서칭을 이용.
        # 노드를 훑으며 모든 노드 `val`을 더한 값과 각 `val`가 담긴 해시맵을 전달.
        # 각 노드에 접근 시, 이때까지의 `val` 총합에서 `targetSum`을 뺀 값이
        # 해시맵에 속하는 지 확인 후, 있다면 가능한 경로가 있음을 의미하므로 +1하는 흐름.

        from collections import defaultdict

        val_map = defaultdict(int)
        ret = 0
        
        def search(node: TreeNode, val_sum: int):
            if not node:
                return

            nonlocal ret
            new_sum = val_sum + node.val
            diff = new_sum - targetSum

            if new_sum == targetSum:
                ret += 1
            if val_map.get(diff):
                ret += val_map.get(diff)

            val_map[new_sum] += 1

            search(node.left, new_sum)
            search(node.right, new_sum)

            val_map[new_sum] -= 1
        
        search(root, 0)
        return ret
