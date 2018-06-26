# !/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/climbing-stairs/description/

假设你正在爬楼梯。需要 n 步你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 步 + 1 步
2.  2 步
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 步 + 1 步 + 1 步
2.  1 步 + 2 步
3.  2 步 + 1 步


经分析发现规律：
1
2
3
5
...

后一个数等于前两个数的和，即斐波那契数列
"""


class Solution:

    def climb_stairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1
        elif n < 0:
            return 0
        f0 = 1
        f1 = 1
        i = 2
        f = 0
        while i <= n:
            f = f0 + f1
            f0 = f1
            f1 = f
            i += 1

        return f


if __name__ == '__main__':
    s = Solution()
    input_num = 3
    result = s.climb_stairs(input_num)
    print(result)
    except_num = 3
    print(result == except_num)
