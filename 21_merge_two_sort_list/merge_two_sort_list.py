# !/usr/bin/env python3
# -*- coding:utf-8 -*-
"""

https://leetcode-cn.com/problems/merge-two-sorted-lists/description/

将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

暂时放弃
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def merge_two_list(self, l1, l2):
        """

        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2

        if l2 is None:
            return l1
        for i in l2:
            l1.append(i)






if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [1, 1, 2, 5, 6]
    s = Solution()
    result_list = [1, 1, 1, 2, 2, 3, 5, 6]
    temp = s.merge_two_list(list1, list2)
    print(temp == result_list)
