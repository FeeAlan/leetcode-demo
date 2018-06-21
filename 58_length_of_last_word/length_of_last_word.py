# !/usr/bin/env python3
# -*- coding:utf-8 -*-
"""

https://leetcode-cn.com/problems/length-of-last-word/description/

给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指由字母组成，但不包含任何空格的字符串。

示例:

输入: "Hello World"
输出: 5
"""


class Solution:
    def length_of_last_word(self, s):
        """
        :type s: str
        :rtype: int
        """
        space = " "
        s = str.strip(s)
        if len(s) == 0:
            return 0
        if space not in s:
            return len(s)
        # 拿到最后一个字符串
        temps = s.split(space)
        return len(temps[-1])


if __name__ == '__main__':
    s = Solution()
    original = "a "
    result = s.length_of_last_word(original)
    print(result == 1)
