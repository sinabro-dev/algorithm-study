"""
https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/

Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.

Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
Output: 6
Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.
"""
class Solution:
    """
    Keyword: Sliding Window
    Space: O(1)
    Time: O(n)
    """
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if len(arr) < k:
            return 0
            
        cnt = 0

        total = 0
        for i in range(k):
            total += arr[i]
        
        if total/k >= threshold:
            cnt += 1

        for i in range(k, len(arr)):
            out = arr[i-k]
            total -= out

            come = arr[i]
            total += come

            if total/k >= threshold:
                cnt += 1
        
        return cnt
