# coding=utf-8

from typing import List


# @solution-sync:begin
class Solution:
    def __init__(self):
        self.output = []

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        symbols = {
            '2': ('a', 'b', 'c'),
            '3': ('d', 'e', 'f'),
            '4': ('g', 'h', 'i'),
            '5': ('j', 'k', 'l'),
            '6': ('m', 'n', 'o'),
            '7': ('p', 'q', 'r', 's'),
            '8': ('t', 'u', 'v'),
            '9': ('w', 'x', 'y', 'z')
        }

        self.backtrack(digits, symbols, 0, '')
        return self.output

    def backtrack(self, digits, symbols, start, path):
        if start == len(digits):
            self.output.append(path)
            return

        cur = digits[start]
        if cur not in symbols:
            return
        for char in symbols[cur]:
            self.backtrack(digits, symbols, start + 1, path + char)


# @solution-sync:end


if __name__ == '__main__':
    digits = "23"

    result = Solution().letterCombinations(digits)
    print(result)
