from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller = ListNode(-1)
        larger = ListNode(-1)

        p = smaller
        q = larger

        i = head
        while i:
            if i.val < x:
                p.next = i
                p = p.next
            else:
                q.next = i
                q = q.next
            i = i.next
        q.next = None
        p.next = larger.next
        return smaller.next
