"""
https://leetcode.com/problems/median-of-two-sorted-arrays/description/

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
"""
class Solution:
    """
    Keyword: Binary Search
    Space: O(1)
    Time: O(log(m+n))
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # L: the number immediately left to the cut
        # R: the number immediately right to the cut
        # For example,  list_size       index of L / R
        #                       1               0 / 0
        #                       2               0 / 1
        #                       3               1 / 1
        #                       4               1 / 2
        #                       5               2 / 2
        #                       6               2 / 3
        #                       7               3 / 3
        #                       8               3 / 4
        # idx_L = (N-1)/2, idx_R = N/2
        # Thus, (L + R) / 2 = ( A[(N-1)/2] + A[N/2] ) / 2
        # Add a few imaginary 'positions'
        # For example,  A1: [# 1 # 2 # 3 # 4 # 5 #] (N1 = 5, N1_Positions = 11)
        #               A2: [# 1 # 1 # 1 # 1 #] (N2 = 4, N2_Posititons = 0)
        # There are always exactly 2*N + 1 'positions' regardless of length N
        # So, idx_L = (CutPosition-1)/2, idx_R = CutPosition/2
        # 
        # There are 2*N1 + 2*N2 + 2 position altogether
        # C1: the cut position in A1
        # C2: the cut position in A2
        # For instance, if C2 = 2, C1 = N1 + N2 - C2 = 7
        # L1 = A1[(C1-1)/2] = 4 | R1 = A1[C1/2] = 4
        # L2 = A2[(C2-1)/2] = 1 | R2 = A2[C2/2] = 1
        #
        # Make sure that any number in lower halves <= any number in upper halves
        # Should be L1 <= R2 and L2 <= R1
        # If L1 > R2, it means there are too many large numbers on the left half of A1,
        #   then must move C1 to the left
        # If L2 > R1, it means there are too many large numbers on the left half of A2,
        #   then must move C2 to the left
        # Otherewise, cut is the correct

        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        size1 = len(nums1)
        size2 = len(nums2)
        
        start = 0
        end = size2 * 2

        while start <= end:
            cut2 = (start + end) // 2
            cut1 = size1 + size2 - cut2

            left1 = nums1[(cut1-1) // 2] if cut1 != 0 else float('-inf')
            right1 = nums1[cut1 // 2] if cut1 != size1*2 else float('inf')

            left2 = nums2[(cut2-1) // 2] if cut2 != 0 else float('-inf')
            right2 = nums2[cut2 // 2] if cut2 != size2*2 else float('inf')
            
            if left1 > right2:
                start = cut2 + 1
            elif left2 > right1:
                end = cut2 - 1
            else:
                return (max(left1, left2) + min(right1, right2)) / 2
        
        return None
