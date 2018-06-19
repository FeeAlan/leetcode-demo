# !/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/implement-strstr/description/

实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
说明:

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。

"""


class Solution:

    @staticmethod
    def str_str(haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0 or needle is None:
            return 0

        if haystack is None or len(haystack) == 0:
            return -1

        if needle not in haystack:
            return -1
        else:
            return haystack.index(needle)


if __name__ == '__main__':
    s = Solution()
    hay = "hello"
    nee = "ll"

    result = s.str_str(hay, nee)
    print(result == 2)
