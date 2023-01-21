"""
https://leetcode.com/problems/restore-ip-addresses/description/

A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.
For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
"""
class Solution:
    """
    Keyword: Backtracking
    Space: O(N^2)
    Time: O(N^2)
    """
    def restoreIpAddresses(self, s: str) -> List[str]:
        if (len(s) < 4) or (len(s) > 12):
            return list()

        cases = list()

        def compose(elems: List[int], size: int):
            if len(elems) == 3:
                if size + sum(elems) == len(s):
                    elems.append(size)
                    cases.append(elems)
                return
            
            for i in range(1, min(4, size)):
                remain = size - i
                cnt = 3 - len(elems)

                if remain > 3 * cnt:
                    continue
                
                l = list(elems)
                l.append(i)
                compose(l, remain)
        
        compose(list(), len(s))

        def valid(s: str) -> bool:
            if (len(s) != 1) and (s[0] == '0'):
                return False
            if (int(s) < 0) or (int(s) > 255):
                return False
            return True
        
        ret = list()

        for case in cases:
            address = ''
            start = 0

            for offset in case:
                sub_s = s[start : start+offset]
                if not valid(sub_s):
                    break
                
                address += ('.' + sub_s)
                start += offset

            if len(address) == len(s) + 4:
                ret.append(address[1:])

        return ret
