from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.prev = -float('inf')

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check(root)

    def check(self, node):
        if not node:
            return True

        left = self.check(node.left)

        if node.val <= self.prev:
            return False

        self.prev = node.val

        right = self.check(node.right)
        return left and right
