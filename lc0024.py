# coding=utf-8

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @solution-sync:begin
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)

        pre = dummy
        cur = head

        while cur and cur.next:
            following = cur.next

            cur.next = following.next
            following.next = cur
            pre.next = following

            pre = cur
            cur = cur.next

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
    head = parse_list_node([1, 2, 3, 4])

    result = Solution().swapPairs(head)
    print(node_to_string(result))