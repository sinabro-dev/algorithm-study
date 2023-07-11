"""
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/

Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.
You can return the answer in any order.

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
"""
class Solution:
    """
    Keyword: BFS
    Space: O(n)
    Time: O(n)
    """
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # 노드들을 모두 훑으며 부모에 대한 포인터를 기록
        # 그리고 target으로부터 BFS를 하며 k만큼 떨어진 노드들을 반환

        from collections import deque

        parents = [None for _ in range(501)]

        queue = deque()
        queue.append((root, None))

        while queue:
            cur, parent = queue.popleft()
            parents[cur.val] = parent

            if cur.left:
                queue.append((cur.left, cur))
            if cur.right:
                queue.append((cur.right, cur))
        
        ret = list()
        visited = set()
        
        queue = deque()
        queue.append((target, 0))

        while queue:
            cur, distance = queue.popleft()

            if distance == k:
                ret.append(cur.val)
                continue
            
            if parents[cur.val] and cur.val not in visited:
                visited.add(cur.val)
                queue.append((parents[cur.val], distance+1))
            if cur.left and cur.left.val not in visited:
                visited.add(cur.left.val)
                queue.append((cur.left, distance+1))
            if cur.right and cur.right.val not in visited:
                visited.add(cur.right.val)
                queue.append((cur.right, distance+1))
        
        return ret


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
