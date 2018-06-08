# !/usr/bin/env python3
# -*- coding:utf-8 -*-
import random
import time


# 计算两数之和
#
# 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
#
# 你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
#
# 例：
# nums = [2,7,5,9,-1]
# target = 9
#
# 结果 [0,1]
#
#


def two_sum(num, target):
    """
    :param num: list[int]  输入数组
    :param target: int   输入的目标值
    :return: list[int]  返回的答案
    """
    if not isinstance(num, list):
        return []
    else:
        temps = []
        for i in range(len(num)):
            cha = target - num[i]
            if cha in temps:
                results = [i, temps.index(cha)]
                return results
            temps.append(num[i])


def random_num(count):
    num = set()
    for i in range(0, count):
        num.add(random.randint(-1000, 1000 * count))

    arr = []
    for i in num:
        arr.append(i)

    arr.insert(10, 97)
    arr.insert(12, 3)
    return arr


def get_current_time():
    return int(time.time() * 1000)


if __name__ == "__main__":
    time0 = get_current_time()
    nums = random_num(100)
    # nums = [2, 7, 11, 15]
    print(nums)
    print("生成随机数消耗时间为:", get_current_time() - time0, " ms")
    target = 100
    # target = 9
    time1 = get_current_time()
    result = two_sum(nums, target)
    print("消耗时间为:", get_current_time() - time1, " ms")
    print(result)
