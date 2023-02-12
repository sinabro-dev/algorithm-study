"""
https://leetcode.com/problems/bitwise-ors-of-subarrays/description/

Given an integer array arr, return the number of distinct bitwise ORs of all the non-empty subarrays of arr.
The bitwise OR of a subarray is the bitwise OR of each integer in the subarray. The bitwise OR of a subarray of one integer is that integer.
A subarray is a contiguous non-empty sequence of elements within an array.

Input: arr = [1,2,4]
Output: 6
Explanation: The possible results are 1, 2, 3, 4, 6, and 7.
"""
class Solution:
    """
    Keyword: DP(Dynamic Programming), Bit Manipulation
    Space: O(n)
    Time: O(30n)
    """
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        # 부분 배열을 하나씩 훑으며, 그 요소들의 OR 결과를 구함.
        # 중복 연산을 줄이기 위해 메모이제이션 활용.
        # M[i][j] = arr[i] | arr[i+1] | ... | arr[j] 라 하고,
        # `arr` 배열 요소들을 훑으며 업데이트 해 나감.
        # 예를 들어 arr[i+1] 요소를 처리할 경우, M[0][i], M[1][i], ... , M[i][i] 까지의
        # 값에 arr[i+1] 요소를 추가하고, arr[i+1] 값 자체도 추가.

        memo = set()
        cals = set()

        for cur in arr:
            memo = {cur | prev for prev in memo}
            memo |= {cur}

            cals |= memo
        
        return len(cals)
