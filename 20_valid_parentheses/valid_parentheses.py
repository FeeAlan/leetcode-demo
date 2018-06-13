# !/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/valid-parentheses/description/

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
"""


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        temp_dict = {"(": ")", "[": "]", "{": "}"}
        stack = []

        for temp_str in s:
            if len(stack) > 0 and stack[-1] in temp_dict and temp_dict[stack[-1]] == temp_str:
                stack.pop()
            else:
                stack.append(temp_str)

        return len(stack) == 0


if __name__ == '__main__':
    s = Solution()
    temp = "(])["
    print(s.isValid(temp))
