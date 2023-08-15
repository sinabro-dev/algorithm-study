"""
https://leetcode.com/problems/partition-list/description/

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.

Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
"""
class Solution:
    """
    Keyword: Two Pointers
    Space: O(n)
    Time: O(n)
    """
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # x 값을 기준으로 두 개의 연결리스트로 구분하여 보관한 다음
        # 모든 노드들을 훑은 후에 두 연결리스트를 연결지음

        small, large = ListNode(-101), ListNode(-101)
        small_start, large_start = small, large
        ptr = head

        while ptr:
            if ptr.val < x:
                small.next = ptr
                small = small.next
            else:
                large.next = ptr
                large = large.next
            
            ptr = ptr.next
        
        small.next = None
        large.next = None
        
        small.next = large_start.next
        return small_start.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
