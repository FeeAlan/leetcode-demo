# !/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/plus-one/description/

给定一个非负整数组成的非空数组，在该数的基础上加一，返回一个新的数组。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
"""


class Solution:

    def plus_one(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for i in range(len(digits)):
            num = num + (digits[i] * 10 ** (len(digits) - i - 1))
        num += 1
        temps = str(num)
        array = []
        for i in temps:
            array.append(int(i))

        print(array)
        return array


if __name__ == '__main__':
    s = Solution()
    arr = [1, 2, 3]
    result = s.plus_one(arr)
    expect = [1, 2, 4]
    print(result == expect)
