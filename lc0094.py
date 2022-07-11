from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        current_node = root
        res = []
        while current_node:
            left_child = current_node.left
            if left_child:
                while left_child.right and left_child.right != current_node:
                    left_child = left_child.right

                if left_child.right != current_node:
                    left_child.right = current_node
                    current_node = current_node.left
                else:
                    # left_child.right = None
                    res.append(current_node.val)
                    current_node = current_node.right
            else:
                res.append(current_node.val)
                current_node = current_node.right

        return res