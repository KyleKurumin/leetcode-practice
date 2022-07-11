# coding=utf-8

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @solution-sync:begin
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        slow, fast = dummy, dummy

        for i in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
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
    head = parse_list_node([1, 2, 3, 4, 5])
    n = 2

    result = Solution().removeNthFromEnd(head, n)
    print(node_to_string(result))