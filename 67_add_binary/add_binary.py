# !/usr/bin/env python3
# -*- coding:utf-8 -*-
"""

https://leetcode-cn.com/problems/add-binary/description/

给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"

"""


class Solution:

    def add_binary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int('0b' + a, 2)
        b = int('0b' + b, 2)
        print(a, b)
        return bin(a + b)[2:]


if __name__ == '__main__':
    s = Solution()
    temp_a = "11"
    temp_b = "1"
    result = s.add_binary(temp_a, temp_b)
    print(result)
    expect = "100"
    print(result == expect)
