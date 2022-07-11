import pprint


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        if len(s1) + len(s2) != len(s3):
            return False

        dp[0][0] = True
        for i in range(1, len(s1) + 1):
            dp[i][0] = s1[i - 1] == s3[i - 1] and dp[i - 1][0]

        for j in range(1, len(s2) + 1):
            dp[0][j] = s2[j - 1] == s3[j - 1] and dp[0][j - 1]

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                dp[i][j] = (s3[i + j - 1] == s1[i - 1] and dp[i - 1][j]) or (
                            s3[i + j - 1] == s2[j - 1] and dp[i][j - 1])

        return dp[-1][-1]