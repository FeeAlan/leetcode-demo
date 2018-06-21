# !/usr/bin/env python3
# -*- coding:utf-8 -*-

"""

https://leetcode-cn.com/problems/maximum-subarray/description/
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6


解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:
如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。



思路：
假设有数组[2,-3,3,2...]
开始遍历数组并累加，第一个数为2 ，第二个数为 -3 ,相加结果为 -1，再加第三个数 3, 相加结果比3小,所以前面的两个数可以去掉

"""
import sys


class Solution:

    def max_sub_array(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return
        if len(nums) == 1:
            return nums[0]
        else:
            max_value = -sys.maxsize
            current_value = 0
            for i in nums:
                if current_value + i <= i:
                    current_value = i
                else:
                    current_value += i
                if max_value < current_value:
                    max_value = current_value

            return max_value


if __name__ == '__main__':
    s = Solution()
    arr = [-2, -1]
    result = s.max_sub_array(arr)
    print(result == -1)
