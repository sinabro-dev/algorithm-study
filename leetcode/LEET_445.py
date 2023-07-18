"""
https://leetcode.com/problems/add-two-numbers-ii/description/

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
"""
class Solution:
    """
    Keyword: Math
    Space: O(n+m)
    Time: O(n+m)
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # l1와 l2에 표현된 노드의 값을 각각 리스트에 기록한다
        # 그리고 덧셈을 위해 자릿수를 맞춰야 하므로 짧은 길이 리스트 앞부분에 요소 0을 필요한만큼 추가한다
        # 이후 각 자리마다 덧셈을 한다

        arr1, arr2 = [0], [0]

        ptr = l1
        while ptr:
            arr1.append(ptr.val)
            ptr = ptr.next
        
        ptr = l2
        while ptr:
            arr2.append(ptr.val)
            ptr = ptr.next
        
        if len(arr1) < len(arr2):
            arr1 = [0] * (len(arr2)-len(arr1)) + arr1
        elif len(arr1) > len(arr2):
            arr2 = [0] * (len(arr1)-len(arr2)) + arr2
        
        arr3 = [0 for _ in range(len(arr1))]
        for i in reversed(range(1, len(arr1))):
            n1, n2 = arr1[i], arr2[i]
            add = n1 + n2

            arr3[i] += (add % 10)
            if arr3[i] >= 10:
                arr3[i-1] += 1
                arr3[i] -= 10
            arr3[i-1] += (add // 10)

        head, ptr = ListNode(), ListNode()
        for i in range(len(arr3)):
            node = ListNode()
            node.val = arr3[i]

            ptr.next = node
            ptr = ptr.next

            if i == 0:
                head = node
        
        while head.next and head.val == 0:
            head = head.next
        
        return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
