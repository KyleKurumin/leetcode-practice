# coding=utf-8

from typing import List

# @solution-sync:begin
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []

        def helper(path, left, right):
            if left == n and right == n:
                ans.append(path)
                return

            if left < n:
                helper(path + '(', left + 1, right)

            if right < left:
                helper(path + ')', left, right + 1)

        helper('', 0, 0)
        return ans
# @solution-sync:end


if __name__ == '__main__':
    n = 3

    result = Solution().generateParenthesis(n)
    print(result)