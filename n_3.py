# coding=utf-8

# Copyright (c) 2018 - <tao.zhang@moji.com>

"""
Author: tao.zhang
Create Date: 2019/2/1
@Software: PyCharm
descirption:
"""
from collections import Counter


def lengthOfLongestSubstring_1(s):
    max_sub_len = 0

    s_len = len(s)

    all_count = Counter(s)
    all_count_num = len(all_count.keys())

    j_pos =1

    for i in range(s_len):
        for j in range(j_pos, s_len+1):
            sub_str = s[i:j]
            sub_counter = Counter(sub_str)
            key_len = len(sub_counter.keys())
            count_sum = sum(sub_counter.values())
            if key_len == count_sum:
                if max_sub_len < len(sub_str):
                    max_sub_len = len(sub_str)
                    j_pos = j
            else:
                break
        if max_sub_len == all_count_num:
            break

    return max_sub_len


def lengthOfLongestSubstring_2(s):
    max_sub_len = 0

    s_len = len(s)

    all_count = Counter(s)
    all_count_num = len(all_count.keys())

    j_pos =1

    for i in range(s_len):
        for j in range(j_pos, s_len+1):
            sub_str = s[i:j]
            if len(set(sub_str)) == len(sub_str):
                if max_sub_len < len(sub_str):
                    max_sub_len = len(sub_str)
                    j_pos = j
            else:
                break
        if max_sub_len == all_count_num:
            break

    return max_sub_len


if __name__ == "__main__":
    msg = "rakwmmnxengbcegiezjhfrbgneoikagdaszofomldsoiyvqcubmbsnjhuaqeayjdrktyzhjczxkasaeodqrxgdfadvgftpk"
    print(lengthOfLongestSubstring_2(msg))
