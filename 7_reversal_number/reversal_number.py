# !/usr/bin/env python3
# -*- coding:utf-8 -*-
import math

"""
https://leetcode-cn.com/problems/reverse-integer/description/

给定一个 32 位有符号整数，将整数中的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。
"""


def reverse(number):
    max = math.pow(2, 31) - 1
    min = -math.pow(2, 31)
    y = 0
    temp = number
    temp = abs(temp)
    while temp != 0:
        x = int(temp % 10)
        y = y * 10 + x
        if y > max or y < min:
            return 0
        temp = int(temp / 10)
    if number > 0:
        return y
    else:
        return -y


if __name__ == "__main__":
    num = 1534236469
    result = 0
    reverse_num = reverse(num)
    print(reverse_num == result)
