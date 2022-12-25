"""
https://leetcode.com/problems/add-two-numbers/description/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    """
    Keyword: Linked List
    Space: O(max(N, M))
    Time: O(max(N, M))
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def deriveNumber(l: Optional[ListNode]) -> int:
            num = 0
            pos = 0
            cur = l

            while True:
                if cur == None:
                    break
                
                num += cur.val * 10**pos
                
                pos += 1
                cur = cur.next
            
            return num

        def buildList(num: int) -> ListNode:
            quo = num
            mod = -1
            start = None
            cur = None

            while True:
                if quo == 0:
                    break
                
                mod = quo % 10
                quo = quo // 10

                if start == None:
                    start = ListNode(mod, None)
                    cur = start
                else:
                    cur.next = ListNode(mod, None)
                    cur = cur.next

            if start == None:
                start = ListNode(0, None)

            return start

        num1 = deriveNumber(l1)
        num2 = deriveNumber(l2)
        return buildList(num1 + num2)
