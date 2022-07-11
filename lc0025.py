# coding=utf-8

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @solution-sync:begin
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        fast = dummy
        slow = dummy
        while fast:
            for _ in range(k):
                fast = fast.next
                if not fast:
                    break

            if not fast:
                break

            follow = fast.next
            fast.next = None
            tail = slow.next
            new_head = self.reverse_link_list(tail)
            slow.next = new_head
            tail.next = follow
            slow = tail
            fast = tail

        return dummy.next

    def reverse_link_list(self, head):
        stack = []
        dummy = ListNode(-1)

        p = head
        while p:
            stack.append(p)
            p = p.next
        q = dummy
        while stack:
            q.next = stack.pop()
            q = q.next
        q.next = None
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
    k = 2

    result = Solution().reverseKGroup(head, k)
    print(node_to_string(result))
