"""
https://leetcode.com/problems/palindrome-linked-list/description/

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
- The number of nodes in the list is in the range [1, 105].
- 0 <= Node.val <= 9

Input: head = [1,2,2,1]
Output: true
"""
class Solution:
    """
    Keyword: Stack, Linked List
    Space: O(n)
    Time: O(n)
    """
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 절반 이전까지는 노드 값을 스택에 저장 후
        # 절반 이후부터는 스택 top 값과 노드 값이 같은지 비교

        cnt = 0
        ptr = head
        while ptr:
            cnt += 1
            ptr = ptr.next
        
        stack = list()
        ptr = head
        for _ in range(cnt // 2):
            stack.append(ptr.val)
            ptr = ptr.next
        
        if cnt % 2 == 1:
            ptr = ptr.next
        
        for _ in range(cnt // 2):
            top = stack.pop()
            if top != ptr.val:
                return False
            ptr = ptr.next

        return True

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
