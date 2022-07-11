from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def helper(path, start):
            if len(path) == k:
                ans.append(path)

            for i in range(start, n + 1):
                helper(path + [i], i + 1)

        helper([], 1)
        return ans