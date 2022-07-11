# coding=utf-8

from typing import List

# @solution-sync:begin
class Solution:
    chs = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)

    def solve(self, board):
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == '.':
                    for c in self.chs:
                        if self.is_valid(board, i, j, c):
                            board[i][j] = c
                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True

    def is_valid(self, board, i, j, c):
        for row in range(len(board)):
            if board[row][j] == c:
                return False

        for col in range(len(board[0])):
            if board[i][col] == c:
                return False

        for x in range((i // 3) * 3, (i // 3) * 3 + 3):
            for y in range((j // 3) * 3, (j // 3) * 3 + 3):
                if board[x][y] == c:
                    return False

        return True
# @solution-sync:end


if __name__ == '__main__':
    board = [
        ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
        ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
        ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
        ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
        ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
    ]
    Solution().solveSudoku(board)
