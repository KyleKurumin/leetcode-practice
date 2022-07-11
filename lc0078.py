from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.backtrack(nums, [], 0, [])

    def backtrack(self, nums, path, start, ans):
        ans.append(path)

        for i in range(start, len(nums)):
            path = path + [nums[i]]
            ans = self.backtrack(nums, path, i + 1, ans)
            path = path[:-1]

        return ans
