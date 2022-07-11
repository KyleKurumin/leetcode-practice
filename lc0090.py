from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []

        def backtrack(path, start, numbers):
            ans.append(path)

            if start == len(numbers):
                return

            visited = set()
            for i in range(start, len(numbers)):
                if numbers[i] in visited:
                    continue

                visited.add(numbers[i])
                backtrack(path + [numbers[i]], i + 1, numbers)

        backtrack([], 0, nums)
        return ans