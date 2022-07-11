from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []

        while matrix:
            ans += matrix.pop(0)
            matrix = list(map(list, zip(*matrix)))[::-1]
        return ans