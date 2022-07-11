
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root):
        current_node = root
        prev = TreeNode(-1 << 31)
        candidates = [None, None]
        is_first_time = True

        while current_node:
            most_right = current_node.left

            if most_right:
                while most_right.right and most_right.right != current_node:
                    most_right = most_right.right

                if most_right.right != current_node:
                    most_right.right = current_node
                    current_node = current_node.left
                else:
                    most_right.right = None
                    if prev.val > current_node.val:
                        if is_first_time:
                            candidates = [prev, current_node]
                        else:
                            candidates[1] = current_node
                        is_first_time = False
                    prev = current_node

                    current_node = current_node.right
            else:
                if prev.val > current_node.val:
                    if is_first_time:
                        candidates = [prev, current_node]
                    else:
                        candidates[1] = current_node
                    is_first_time = False
                prev = current_node

                current_node = current_node.right

        candidates[0].val, candidates[1].val = candidates[1].val, candidates[0].val