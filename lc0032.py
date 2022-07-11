# coding=utf-8


# @solution-sync:begin
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * len(s)
        result = 0

        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2
                else:
                    if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                        dp[i] = dp[i - dp[i - 1] - 2] + dp[i - 1] + 2

            result = max(result, dp[i])
        return result
# @solution-sync:end


if __name__ == '__main__':
    s = "(()"

    result = Solution().longestValidParentheses(s)
    print(result)