"""
https://leetcode.com/problems/intersection-of-two-linked-lists/description/

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
The test cases are generated such that there are no cycles anywhere in the entire linked structure.
Note that the linked lists must retain their original structure after the function returns.
- The number of nodes of listA is in the m.
- The number of nodes of listB is in the n.
- 1 <= m, n <= 3 * 104
- 1 <= Node.val <= 105
- 0 <= skipA < m
- 0 <= skipB < n
- intersectVal is 0 if listA and listB do not intersect.
- intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
Note that the intersected node's value is not 1 because the nodes with value 1 in A and B (2nd node in A and 3rd node in B) are different node references. In other words, they point to two different locations in memory, while the nodes with value 8 in A and B (3rd node in A and 4th node in B) point to the same location in memory.
"""
class Solution:
    """
    Keyword: Linked List, Two Points
    Space: O(1)
    Time: O(m+n)
    """
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 두 리스트가 결국에는 마지막에 하나로 합쳐지기 때문에
        # 각 리스트를 역으로 훑다가 쪼깨지는 순간이 존재하게 됨
        # 다만 이럴 경우 역방향 포인터가 필요하므로
        # 이 방법보다는 각 리스트의 길이를 구해놓고
        # 더 짧은 리스트의 head를 시점으로 하여
        # 같은 노드를 가르킬 때까지 나아가면 됨

        n1, ptr1 = 0, headA
        while ptr1:
            n1 += 1
            ptr1 = ptr1.next
        
        n2, ptr2 = 0, headB
        while ptr2:
            n2 += 1
            ptr2 = ptr2.next
        
        ptr1, ptr2 = headA, headB
        
        if n1 > n2:
            for _ in range(n1-n2):
                ptr1 = ptr1.next
        elif n1 < n2:
            for _ in range(n2-n1):
                ptr2 = ptr2.next
        
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None        
