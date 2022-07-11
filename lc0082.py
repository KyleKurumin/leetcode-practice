from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)

        p, q = dummy, head

        while q and q.next:
            if q.next.val == q.val:
                while q and q.next and q.next.val == q.val:
                    q = q.next
                p.next = q.next
                q = q.next
            else:
                p = p.next
                q = q.next
        return dummy.next
