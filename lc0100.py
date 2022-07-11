from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if (not p and q) or (not q and p):
            return False

        if p.val != q.val:
            return False

        lv = self.isSameTree(p.left, q.left)
        rv = self.isSameTree(p.right, q.right)

        return lv and rv
