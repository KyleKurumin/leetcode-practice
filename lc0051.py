class Solution:
    def __init__(self):
        self.output = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.backtrack([], 0, n, set())
        return self.output

    def backtrack(self, board, start, n, visited):
        if start == n:
            self.output.append(board.copy())
            return

        for i in range(n):
            if self.check(visited, start, i):
                board.append('.' * i + 'Q' + '.' * (n - i - 1))
                visited.add((start, i))
                self.backtrack(board, start + 1, n, visited)
                board.pop()
                visited.discard((start, i))

    def check(self, visited, x, y):
        for row, col in visited:
            if col == y or abs(col - y) == x - row:
                return False
        return True
