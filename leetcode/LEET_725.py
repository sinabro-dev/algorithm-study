"""
https://leetcode.com/problems/split-linked-list-in-parts/description/?envType=daily-question&envId=2023-09-06

Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.
The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.
The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.
Return an array of the k parts.
- The number of nodes in the list is in the range [0, 1000].
- 0 <= Node.val <= 1000
- 1 <= k <= 50
 
Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
Output: [[1,2,3,4],[5,6,7],[8,9,10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
"""
class Solution:
    """
    Keyword: Linked List
    Space: O(1)
    Time: O(n)
    """
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        size = 0
        ptr = head
        while ptr:
            size += 1
            ptr = ptr.next
        
        bigs = size - (size // k) * k
        smalls = k - bigs
        
        parts = [None for _ in range(k)]
        ptr = head

        for i in range(k):
            tail = None
            parts[i] = ptr

            if i < bigs:
                iters = size//k + 1
            else:
                iters = size//k
            
            for _ in range(iters):
                tail = ptr
                ptr = ptr.next
            
            if tail != None: tail.next = None
            
        return parts

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
