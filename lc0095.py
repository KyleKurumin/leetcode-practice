# Definition for a binary tree node.

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.build_tree(1, n)

    def build_tree(self, start, end):
        res = []
        if start > end:
            return [None]

        for i in range(start, end + 1):
            left_list = self.build_tree(start, i - 1)
            right_list = self.build_tree(i + 1, end)
            for left in left_list:
                for right in right_list:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    res.append(root)

        return res
