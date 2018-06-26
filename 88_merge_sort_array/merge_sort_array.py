# !/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
https://leetcode-cn.com/problems/merge-sorted-array/description/

给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]

"""


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                if i == len(nums1) - 1:
                    while j < n:
                        nums1.append(nums2[j])
                        j += 1
                else:
                    i += 1
            else:
                if i == 0:
                    index = 0
                else:
                    index = i - 1
                nums1.insert(index, nums2[j])
                j += 1
                m += 1

        return nums1


if __name__ == '__main__':
    s = Solution()
    arr1 = [1, 2, 3]
    temp_m = 3
    arr2 = [2, 5, 6]
    temp_n = 3
    result = s.merge(arr1, temp_m, arr2, temp_n)
    print(result)
    except_result = [1, 2, 2, 3, 5, 6]
    print(result == except_result)
