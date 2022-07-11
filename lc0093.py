from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []

        def helper(path, start):
            if start == len(s):
                if len(path) == 4:
                    ans.append(path)
                return

            if len(s) - start > 3 * (4 - len(path)):
                return

            if s[start] == '0':
                helper(path + [s[start]], start + 1)
                return

            for i in range(start, len(s)):
                if 0 < int(s[start: i + 1]) <= 255:
                    helper(path + [s[start:i + 1]], i + 1)

        helper([], 0)
        return list(map(lambda x: '.'.join(x), ans))