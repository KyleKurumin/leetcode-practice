# coding=utf-8


# @solution-sync:begin
import pprint


class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = '#'.join(list(s))
        s = '#' + s + '#'

        dp = [0] * len(s)
        l, r = 0, 0
        dp[0] = 1
        for i in range(1, len(s)):
            if i <= r:
                dp[i] = min(dp[l + r - i], r - i + 1)
            while i - dp[i] >= 0 and i + dp[i] < len(s) and s[i + dp[i]] == s[i - dp[i]]:
                dp[i] += 1
            if i + dp[i] - 1 > r:
                l = i - dp[i] + 1
                r = i + dp[i] - 1

        center = max(range(len(dp)), key=lambda x: dp[x])

        longest = ''.join(x for x in s[center - dp[center] + 1: center + dp[center]] if x != '#')
        return longest
# @solution-sync:end


if __name__ == '__main__':
    s = "babad"

    result = Solution().longestPalindrome(s)
    print(result)