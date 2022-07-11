# coding=utf-8

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @solution-sync:begin
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]

        output = []

        for i in range(0, len(lists), 2):
            p1 = lists[i]
            p2 = lists[i + 1] if i + 1 < len(lists) else None
            output.append(self.merge_two(p1, p2))

        return self.mergeKLists(output)

    def merge_two(self, link1, link2):
        p = link1
        q = link2
        dummy = ListNode(-1)
        a = dummy

        while p and q:
            if p.val < q.val:
                a.next = p
                p = p.next
            else:
                a.next = q
                q = q.next
            a = a.next

        rest = p or q
        a.next = rest
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
    lists = [
        parse_list_node([1, 4, 5]),
        parse_list_node([1, 3, 4]),
        parse_list_node([2, 6]),
    ]

    result = Solution().mergeKLists(lists)
    print(node_to_string(result))