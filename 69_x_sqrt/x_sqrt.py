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
import math


class Solution:
    def my_sqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(math.sqrt(x))



if __name__ == '__main__':
    s = Solution()
    temp_x = 132923432
    result = s.my_sqrt(temp_x)
    expect = 11529
    print(result == expect)
