from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        output = []

        def dfs(path, state=0):
            if len(path) == len(nums):
                output.append(path)
                return

            layer = set()
            for i, num in enumerate(nums):
                if state & (1 << i) == 0 and num not in layer:
                    layer.add(num)
                    dfs(path + [num], state | (1 << i))

        dfs([], 0)
        return output
