# coding=utf-8

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @solution-sync:begin
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        k = dummy
        p = l1
        q = l2

        addition = 0
        while p and q:
            temp = p.val + q.val + addition
            value = temp % 10
            addition = temp // 10

            k.next = ListNode(value)
            k = k.next
            p = p.next
            q = q.next

        r = p or q
        while r:
            temp = r.val + addition
            addition = temp // 10
            value = temp % 10
            k.next = ListNode(value)
            r = r.next
            k = k.next

        if addition > 0:
            k.next = ListNode(addition)

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
    l1 = parse_list_node([2, 4, 3])
    l2 = parse_list_node([5, 6, 4])

    result = Solution().addTwoNumbers(l1, l2)
    print(node_to_string(result))