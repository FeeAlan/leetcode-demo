# !/usr/bin/env python3
# -*- coding:utf-8 -*-
"""

https://leetcode-cn.com/problems/sqrtx/description/

实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。
"""


class Solution:
    def my_sqrt(self, x):
        """
        对于一个非负数n，其平方根不会大于n/2+1(注意小数，会导致算法失败)
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        i = 1
        j = x / 2 + 1
        while i <= j:
            center = int((i + j) / 2)
            if center ** 2 == x:
                return center
            elif center ** 2 > x:
                j = center - 1
            else:
                i = center + 1
        return j


if __name__ == '__main__':
    s = Solution()
    temp_x = 36
    result = s.my_sqrt(temp_x)
    print(result)
    expect = 6
    print(result == expect)
