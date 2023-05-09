"""
https://leetcode.com/problems/swap-nodes-in-pairs/description/

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Input: head = [1,2,3,4]
Output: [2,1,4,3]
"""
class Solution:
    """
    Keyword: Linked List
    Space: O(1)
    Time: O(n)
    """
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        prev = dummy

        while True:
            if not prev.next:
                break
            if not prev.next.next:
                break
            
            cur = prev.next
            follow = prev.next.next

            prev.next = follow
            cur.next = follow.next
            follow.next = cur

            prev = prev.next.next
        
        head = dummy.next
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
