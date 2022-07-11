from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        base = [0] * len(matrix[0])
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                base[j] = 0 if matrix[i][j] == '0' else base[j] + int(matrix[i][j])

            temp = [0] + base + [0]

            stack = []
            for j in range(len(temp)):
                while stack and temp[stack[-1]] > temp[j]:
                    idx = stack.pop()
                    height = temp[idx]
                    width = j - stack[-1] - 1
                    res = max(res, height * width)
                stack.append(j)
        return res