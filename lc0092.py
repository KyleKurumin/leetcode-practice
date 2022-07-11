from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        p = dummy
        for _ in range(left - 1):
            p = p.next

        tail = p.next
        for _ in range(right - left):
            cur = tail.next
            following = p.next
            tail.next = cur.next

            p.next = cur
            cur.next = following
        return dummy.next
