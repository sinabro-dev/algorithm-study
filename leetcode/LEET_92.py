"""
https://leetcode.com/problems/reverse-linked-list-ii/description/

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
- The number of nodes in the list is n.
- 1 <= n <= 500
- 500 <= Node.val <= 500
- 1 <= left <= right <= n

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
"""
class Solution:
    """
    Keyword: Linked List
    Spcae: O(1)
    Time: O(n)
    """
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        left_before, right_after = ListNode(), None

        prev_ptr = None
        cur_ptr = head
        idx = 1

        while idx < left:
            left_before = cur_ptr
            cur_ptr = cur_ptr.next
            idx += 1
        
        sub_start = cur_ptr
        sub_end = cur_ptr

        while idx < right:
            cur_ptr = cur_ptr.next
            idx += 1
            right_after = cur_ptr.next
        
        if not right_after:
            right_after = cur_ptr.next
        
        cur_ptr.next = None
        left_before.next = right_after

        prev_ptr = sub_start
        cur_ptr = sub_start.next
        prev_ptr.next = None

        while cur_ptr:
            tmp = cur_ptr.next
            cur_ptr.next = prev_ptr
            prev_ptr = cur_ptr
            cur_ptr = tmp
            sub_start = prev_ptr
        
        left_before.next = sub_start
        sub_end.next = right_after

        if left == 1:
            head = sub_start

        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
