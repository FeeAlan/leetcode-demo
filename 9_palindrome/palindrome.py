# !/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true


示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。

进阶:

你能不将整数转为字符串来解决这个问题吗？

"""
import math


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


def is_palindrome(num):
    if num < 0:
        return False
    else:
        return reverse(num) == num


if __name__ == "__main__":
    num = -121
    print(is_palindrome(num))