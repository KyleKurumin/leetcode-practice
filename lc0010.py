# coding=utf-8


# @solution-sync:begin
import pprint


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]

        dp[0][0] = True

        for i in range(1, len(p) + 1):
            if p[i - 1] == '*':
                dp[i][0] = dp[i - 2][0]

        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] == '*':
                    if p[i - 2] == '.' or p[i - 2] == s[j - 1]:
                        dp[i][j] = dp[i - 2][j] | dp[i][j - 1]
                    else:
                        dp[i][j] = dp[i - 2][j]
                elif p[i - 1] == '.' or p[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[-1][-1]
# @solution-sync:end


if __name__ == '__main__':
    s = "aa"
    p = "a"

    result = Solution().isMatch(s, p)
    print(result)
