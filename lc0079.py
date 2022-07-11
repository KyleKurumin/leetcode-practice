from typing import List


class Solution:
    def __init__(self):
        self.directions = ((1, 0), (-1, 0), (0, -1), (0, 1))

    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.dfs(board, (i, j), word, {(i, j)}, 1):
                    return True

        return False

    def dfs(self, board, position, target, visited, i):
        if i == len(target):
            return True
        m, n = len(board), len(board[0])
        x, y = position

        result = False
        for offset_x, offset_y in self.directions:
            new_x, new_y = x + offset_x, y + offset_y
            if not (0 <= new_x < m) or not (0 <= new_y < n) or (new_x, new_y) in visited or board[new_x][new_y] != \
                    target[i]:
                continue
            visited.add((new_x, new_y))
            result |= self.dfs(board, (new_x, new_y), target, visited, i + 1)
            visited.discard((new_x, new_y))
        return result