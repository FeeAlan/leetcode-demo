# !/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/count-and-say/description/

报数序列是指一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n ，输出报数序列的第 n 项。

注意：整数顺序将表示为一个字符串。

示例 1:

输入: 1
输出: "1"


示例 2:

输入: 4
输出: "1211"
"""


class Solution:

    def count_and_say(self, n):
        """
        :type n: int
        :rtype: str
        """
        temp = "1"
        for i in range(1, n):
            temp_next = ""
            j, m = 0, len(temp)
            count = 1
            while j < m:
                current = temp[j]
                if j < m - 1:
                    next_str = temp[j + 1]
                else:
                    next_str = ""
                if current == next_str:
                    count = count + 1
                else:
                    temp_next = temp_next + str(count) + current
                    count = 1
                j = j + 1

            temp = temp_next
            print(temp)
        return temp


if __name__ == '__main__':
    s = Solution()
    num = 6
    result = s.count_and_say(num)
    print(result == "312211")
