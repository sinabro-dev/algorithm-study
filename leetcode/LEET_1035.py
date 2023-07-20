"""
https://leetcode.com/problems/uncrossed-lines/description/

You are given two integer arrays nums1 and nums2. We write the integers of nums1 and nums2 (in the order they are given) on two separate horizontal lines.
We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:
- nums1[i] == nums2[j], and
- the line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).
Return the maximum number of connecting lines we can draw in this way.

Input: nums1 = [1,4,2], nums2 = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from nums1[1] = 4 to nums2[2] = 4 will intersect the line from nums1[2]=2 to nums2[1]=2.
"""
class Solution:
    """
    Keyword: Recursion, Dynamic Programming
    Space: O(n*m)
    Time: O(n*m)
    """
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # 그리디하게 문제 접근하면 최대 선분 숫자를 구할 수 없음
        # 모든 경우를 확인해서 답을 구해야 함
        # 재귀를 이용
        # 1) i1 요소값과 i2 요소값이 같은 경우 cnt++ 후, i1++와 i2++ 수행
        # 2) i1 요소값과 i2 요소값이 다른 경우
        #   - i1++ 수행 후 재귀
        #   - i2++ 수행 후 재귀
        #   - 두 재귀의 결과 중 최댓값만큼 cnt에 덧셈
        # ---------------------------------------------------------------------------
        # 다이나믹 프로그래밍을 이용
        # memo[i][j]는 아래처럼 정의
        # 1) nums1[i] == nums2[j] 이면, 1 + memo[i-1][j-1]
        # 2) nums1[i] != nums2[j] 이면, max(memo[i-1][j], memo[i][j-1])

        def use_recursion_with_memo() -> int:
            memo = [[-1] * len(nums2) for _ in range(len(nums1))]
        
            def do(i, j: int) -> int:
                if (i == len(nums1)) or (j == len(nums2)):
                    return 0
                
                if memo[i][j] != -1:
                    return memo[i][j]
                
                cnt = 0
                if nums1[i] == nums2[j]:
                    cnt = 1 + do(i+1, j+1)
                else:
                    cnt += max(do(i+1, j), do(i, j+1))
                
                memo[i][j] = cnt
                return cnt
            
            return do(0, 0)
        
        def use_dynamic_programming() -> int:
            n1, n2 = len(nums1), len(nums2)

            memo = [[-1] * (n2+1) for _ in range(n1+1)]
            for i in range(n1+1):
                memo[i][0] = 0
            for j in range(n2+1):
                memo[0][j] = 0
            
            for i in range(1, n1+1):
                for j in range(1, n2+1):
                    cnt = 0

                    if nums1[i-1] == nums2[j-1]:
                        cnt = 1 + memo[i-1][j-1]
                    else:
                        cnt = max(memo[i-1][j], memo[i][j-1])

                    memo[i][j] = cnt
            
            return memo[-1][-1]

        # use_recursion_with_memo()
        return use_dynamic_programming()
