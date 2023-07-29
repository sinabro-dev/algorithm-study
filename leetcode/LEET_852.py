"""
https://leetcode.com/problems/peak-index-in-a-mountain-array/description/

An array arr a mountain if the following properties hold:
- arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
- arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
- arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].
You must solve it in O(log(arr.length)) time complexity.

Input: arr = [0,10,5,2]
Output: 1
"""
class Solution:
    """
    Keyword: Binary Search
    Space: O(1)
    Time: O(log n)
    """
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # 이진 탐색을 해가며 앞뒤 요소의 변화가 증가인지 감소인지 여부에 따라
        # 탐색 범위를 좁혀가고, 앞뒤 요소 변화가 역전되는 곳을 찾을 때까지 반복 수행

        start, end = 0, len(arr)-1
        while (start < end) and (end - start >= 2):
            mid = (start+end) // 2

            if arr[mid-1] < arr[mid] and arr[mid] < arr[mid+1]:
                start = mid
            elif arr[mid-1] > arr[mid] and arr[mid] > arr[mid+1]:
                end = mid
            else:
                return mid
        
        return -1
