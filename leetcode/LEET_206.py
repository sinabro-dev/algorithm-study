"""
https://leetcode.com/problems/reverse-linked-list/description/

Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""
class Solution:
    """
    Keyword: Recursion, Two Pointers
    Space: O(1)
    Time: O(n)
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = None
        second = head

        while second:
            tmp = second.next
            second.next = first

            first = second
            second = tmp
            
        return first
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
