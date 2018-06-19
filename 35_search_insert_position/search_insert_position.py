# !/usr/bin/env python3
# -*- coding:utf-8 -*-

"""

https://leetcode-cn.com/problems/search-insert-position/description/

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0
"""


class Solution:

    def search_insert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(0, len(nums)):
            if target == nums[i]:
                return i
            elif target < nums[i]:
                if i - 1 < 0:
                    return 0
                else:
                    return i
            else:
                if i == len(nums) - 1:
                    return i + 1
                else:
                    continue


if __name__ == '__main__':
    s = Solution()
    num = [1, 3, 5, 6]

    temp = 2

    result = s.search_insert(num, temp)
    print(result == 1)
