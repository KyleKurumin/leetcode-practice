from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = grid[0][:]

        for i in range(1, len(grid[0])):
            dp[i] = dp[i - 1] + grid[0][i]

        for i in range(1, len(grid)):
            for j in range(len(grid[0])):
                if j == 0:
                    dp[j] = dp[j] + grid[i][j]
                else:
                    dp[j] = min(dp[j - 1], dp[j]) + grid[i][j]

        return dp[-1]