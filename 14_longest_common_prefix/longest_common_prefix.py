# !/usr/bin/env python3
# -*- coding:utf-8 -*-
"""

https://leetcode-cn.com/problems/longest-common-prefix/description/

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"


示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

"""


class Solution(object):
    """
    @:param arr 数据
    """

    def common_prefix(self, arr):
        if arr is None or len(arr) == 0:
            return ""
        elif len(arr) == 1:
            return arr[0]
        else:
            arr = sorted(arr, key=len)
            print(arr)
            # 默认第一个为最长公共前缀
            i = 0
            prefix = ""
            result = arr[0]
            while True:
                try:
                    temp = result[i]
                    for str in arr:
                        if str[i] != temp:
                            return prefix
                except:
                    return prefix
                prefix += temp
                i += 1

            return prefix


if __name__ == '__main__':
    temp = ["aa", "aabb", "aabbccdd", "aa", "aa"]
    s = Solution()
    result = s.common_prefix(temp)
    print(result)