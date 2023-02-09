"""
https://leetcode.com/problems/check-if-n-and-its-double-exist/description/

Given an array arr of integers, check if there exist two indices i and j such that :
- i != j
- 0 <= i, j < arr.length
- arr[i] == 2 * arr[j]

Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
"""
class Solution:
    """
    Keyword: Binary Search, Hash
    Space: O(n)
    Time: O(log n)
    """
    def checkIfExist(self, arr: List[int]) -> bool:
        # `arr` 정렬 후, 이진 탐색으로 조건에 맞는 요소 존재하는 지 훑음.
        
        arr.sort()

        def search(target: int, left: int, right: int) -> bool:
            while left <= right:
                mid = left + (right - left) // 2
                if arr[mid] < target:
                    left = mid + 1
                elif arr[mid] > target:
                    right = mid - 1
                else:
                    return True
            return False
        
        for idx in reversed(range(len(arr))):
            num = arr[idx]

            if num % 2 != 0:
                continue

            if num < 0:
                left, right = idx + 1, len(arr) - 1
            else:
                left, right = 0, idx - 1

            if search(num // 2, left, right):
                return True
        
        return False
