"""
https://leetcode.com/problems/linked-list-cycle-ii/description/

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
Do not modify the linked list.
- The number of the nodes in the list is in the range [0, 104].
- 105 <= Node.val <= 105
- pos is -1 or a valid index in the linked-list
 
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
"""
class Solution:
    """
    Keyword: Two Pointers, Floyd's Cycle
    Space: O(1)
    Time: O(v)
    """
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Floyd's Cycle Detection 알고리즘 사용

        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                slow = head
                break
        
        if not fast or not fast.next or slow != head:
            return None
        
        while fast != slow:
            fast = fast.next
            slow = slow.next
        
        return slow

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
