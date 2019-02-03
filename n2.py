# coding=utf-8

# Copyright (c) 2018 - <tao.zhang@moji.com>

"""
Author: tao.zhang
Create Date: 2019/2/1
@Software: PyCharm
descirption:
"""


def addTwoNumbers_1(l1, l2):
    n_list = []
    n_v = 0

    l1_len = len(l1)
    l2_len = len(l2)

    min_len, larget_list = (l1_len, l2) if l1_len <= l2_len else (l2_len, l1)
    for i in range(min_len):
        v_tmp = l1[i] + l2[i] + n_v
        if v_tmp >= 10:
            v = v_tmp%10
            n_v = 1
        else:
            v = v_tmp
            n_v = 0
        n_list.append(v)

    if n_v == 0:
        n_list.extend(larget_list[min_len:])
    else:
        for i in range(min_len, len(larget_list)):
            v_tmp = larget_list[i] + n_v
            if v_tmp >= 10:
                v = v_tmp%10
                n_v = 1
            else:
                v = v_tmp
                n_v = 0
            n_list.append(v)

    return n_list


def addTwoNumbers_2(l1, l2):

    if l1.val == 0:
        return l2

    if l2.val == 0:
        return l1

    l1_ptr = l1
    l2_ptr = l2
    ptr = None

    n_v = 0

    while l1_ptr is not None or l2_ptr is not None:

        if l1_ptr is not None and l2_ptr is not None:
            v_tmp = l1_ptr.val  + l2_ptr.val + n_v
            if v_tmp >= 10:
                v = v_tmp%10
                n_v = 1
            else:
                v = v_tmp
                n_v = 0
            if ptr is None:
                dummyRoot = ListNode(v)
                ptr = dummyRoot
            ptr.next = ListNode(v)
            ptr = ptr.next
            l1_ptr = l1_ptr.next
            l2_ptr = l1_ptr.next
        elif l1_ptr is not None:
            v_tmp = l1_ptr.val  + n_v
            if v_tmp >= 10:
                v = v_tmp%10
                n_v = 1
            else:
                v = v_tmp
                n_v = 0
            ptr.next = ListNode(v)
            ptr = ptr.next
            l1_ptr = l1_ptr.next
        elif l2_ptr is not None:
            v_tmp = l2_ptr.val + n_v
            if v_tmp >= 10:
                v = v_tmp % 10
                n_v = 1
            else:
                v = v_tmp
                n_v = 0
            ptr.next = ListNode(v)
            ptr = ptr.next
            l2_ptr = l1_ptr.next

    return ptr


if __name__ == "__main__":
    l1 = [2, 4, 3, 4]
    l2 = [5, 6, 4]
    print(addTwoNumbers_2(l1, l2))