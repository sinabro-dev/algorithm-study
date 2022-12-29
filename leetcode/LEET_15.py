"""
https://leetcode.com/problems/3sum/description/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
"""
class Solution:
    """
    Keyword: Combination
    Space: O(N)
    Time: O(N^2)
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 기본적으로 nC3 Combination을 이용.
        # 다만 이렇게 하면 O(N^3)이기 때문에 비효율적.
        # 각 경우를 반복하면서 중복되는 조합을 걸러내서 넘어가도록 하는 과정이 핵심일 듯.
        # `nums`를 이루는 수들을 음수, 0, 양수 집합으로 구분하며, 각 요소가 몇 개 있는 지 조사.
        # 가능한 조합의 경우인 (음, 음, 양), (음, 0, 양), (음, 양, 양), (0, 0, 0) 을 확인.

        def insert_to_map(mapping: dict, key: int):
            val = mapping.get(key)
            if not val:
                mapping[key] = 1
            else:
                mapping[key] = val + 1

        n_cnt_map = dict()
        p_cnt_map = dict()
        zero_cnt = 0

        for num in nums:
            if num < 0:
                insert_to_map(n_cnt_map, num)
            elif num > 0:
                insert_to_map(p_cnt_map, num)
            else:
                zero_cnt += 1
        
        ret = []

        if zero_cnt >= 3:
            ret.append([0, 0, 0])

        if zero_cnt >= 1:
            for num in list(n_cnt_map.keys()):
                if -num in p_cnt_map:
                    ret.append([num, 0, -num])

        def find_cases(cnt_list: list, opp_cnt_map: dict):
            for cur_idx, pair in enumerate(cnt_list):
                (cur_num, cur_cnt) = pair

                if cur_cnt >= 2:
                    opp_num = -(cur_num * 2)
                    (opp_num in opp_cnt_map) and ret.append([cur_num, cur_num, opp_num])

                for next_idx in range(cur_idx + 1, len(cnt_list)):
                    (next_num, _) = cnt_list[next_idx]

                    opp_num = -(cur_num + next_num)
                    (opp_num in opp_cnt_map) and ret.append([cur_num, next_num, opp_num])

        find_cases(list(n_cnt_map.items()), p_cnt_map)
        find_cases(list(p_cnt_map.items()), n_cnt_map)

        return ret
