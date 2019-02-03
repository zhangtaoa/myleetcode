# coding=utf-8

# Copyright (c) 2018 - <tao.zhang@moji.com>

"""
Author: tao.zhang
Create Date: 2019/2/1
@Software: PyCharm
descirption:
"""


def add_num_1(nums, target):
    nums_len = len(nums)
    for i in range(nums_len):
        for j in range(i+1, nums_len):
            if nums[i] + nums[j] == target:
                return i, j


def add_num_2(nums, target):
    nums_len = len(nums)
    for i in range(nums_len):
        other_value = target - nums[i]
        if other_value in nums:
            other_index = nums.index(other_value)
            if i != other_index:
                return i, other_index


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 26
    print(add_num_2(nums, target))
