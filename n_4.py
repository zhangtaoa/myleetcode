# coding=utf-8

# Copyright (c) 2018 - <tao.zhang@moji.com>

"""
Author: tao.zhang
Create Date: 2019/2/1
@Software: PyCharm
descirption:
"""


def findMedianSortedArrays_1(nums1, nums2):
    nums1.extend(nums2)
    nums1.sort()
    nums1_len = len(nums1)
    print(nums1)
    mid_pos_1 = nums1_len/2.0
    mid_pos_2 = nums1_len/2
    if mid_pos_1 == mid_pos_2:
        print(mid_pos_2)
        return (nums1[mid_pos_2-1]+nums1[mid_pos_2])/2.0
    else:
        return nums1[mid_pos_2]/1.0


def findMedianSortedArrays_2(nums1, nums2):
    nums1.extend(nums2)
    nums1.sort()
    nums1_len = len(nums1)
    print(nums1)
    mid_pos_1 = nums1_len%2
    mid_pos_2 = nums1_len/2
    if not mid_pos_1:
        print(mid_pos_2)
        return (nums1[mid_pos_2-1]+nums1[mid_pos_2])/2.0
    else:
        return nums1[mid_pos_2]/1.0

if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(findMedianSortedArrays_2(nums1, nums2))