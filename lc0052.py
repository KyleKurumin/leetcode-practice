class Solution:
    def __init__(self):
        self.output = 0

    def totalNQueens(self, n: int) -> int:
        self.backtrack(0, n, set())
        return self.output

    def backtrack(self, start, n, visited):
        if start == n:
            self.output += 1
            return

        for i in range(n):
            if self.check(visited, start, i):
                visited.add((start, i))
                self.backtrack(start + 1, n, visited)
                visited.discard((start, i))

    def check(self, visited, x, y):
        for row, col in visited:
            if col == y or abs(col - y) == x - row:
                return False
        return True

