from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        length = 0
        p = head
        while p:
            p = p.next
            length += 1
        k = k % length

        if k == 0:
            return head

        slow = head
        fast = head

        for _ in range(k):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        return_node = slow.next
        slow.next = None
        fast.next = head

        return return_node
