"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Keyword: Two Pointers
    Space: O(1)
    Time: O(N)
    """
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 이 문제의 핵심은 되돌아오는 과정없이 한 번에 해결할 수 있는가 이다.
        # 현재 노드를 가리키는 포인터와 `n` 이후 노드를 가리키는 포인터를 두어서,
        # `n` 이후 노드가 마지막 노드인 확인하며 반복을 진행하는 흐름.

        cur = head
        jump = head
        for _ in range(n):
            jump = jump.next

        if not jump:
            return None if n == 1 else head.next

        while jump.next:
            cur = cur.next
            jump = jump.next
        
        if n == 1:
            cur.next = None
        else:
            cur.next = cur.next.next
        return head
