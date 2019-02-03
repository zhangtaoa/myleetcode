# Definition for singly-linked list.


import json

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1.val == 0 and l1.next is None:
            return l2

        if l2.val == 0 and l2.next is None:
            return l1

        l1_ptr = l1
        l2_ptr = l2
        ptr = None

        n_v = 0

        while l1_ptr is not None or l2_ptr is not None:

            if l1_ptr is not None and l2_ptr is not None:
                v_tmp = l1_ptr.val + l2_ptr.val + n_v
                if v_tmp >= 10:
                    v = v_tmp % 10
                    n_v = 1
                else:
                    v = v_tmp
                    n_v = 0
                if ptr is None:
                    dummyRoot = ListNode(v)
                    ptr = dummyRoot
                else:
                    ptr.next = ListNode(v)
                    ptr = ptr.next
                l1_ptr = l1_ptr.next
                l2_ptr = l2_ptr.next
            elif l1_ptr is not None:
                v_tmp = l1_ptr.val + n_v
                if v_tmp >= 10:
                    v = v_tmp % 10
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
                l2_ptr = l2_ptr.next

        if n_v == 1:
            ptr.next = ListNode(n_v)

        return dummyRoot


def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.next()
            l1 = stringToListNode(line)
            line = lines.next()
            l2 = stringToListNode(line)

            ret = Solution().addTwoNumbers(l1, l2)

            out = listNodeToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()