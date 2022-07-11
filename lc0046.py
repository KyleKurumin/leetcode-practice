from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        available = set(nums)

        def dfs(path):
            if len(path) == len(nums):
                output.append(path)
                return

            for num in nums:
                if num in available:
                    available.discard(num)
                    dfs(path + [num])
                    available.add(num)

        dfs([])
        return output