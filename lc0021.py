# coding=utf-8

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @solution-sync:begin
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(-1)
        k = dummy
        p = list1
        q = list2

        while p and q:
            if p.val <= q.val:
                k.next = p
                p = p.next
            else:
                k.next = q
                q = q.next
            k = k.next
        if p:
            k.next = p
        if q:
            k.next = q
        return dummy.next


# @solution-sync:end


def parse_list_node(param):
    head = None
    tail = None
    for i in param:
        node = ListNode(i)
        if head is None:
            head = node
        else:
            tail.next = node
        tail = node
    return head


def node_to_string(h):
    buf = '['
    c = h
    while c:
        buf = buf + str(c.val)
        if c.next:
            buf = buf + ','
        c = c.next
    buf = buf + ']'
    return buf


if __name__ == '__main__':
    list1 = parse_list_node([1, 2, 4])
    list2 = parse_list_node([1, 3, 4])

    result = Solution().mergeTwoLists(list1, list2)
    print(node_to_string(result))