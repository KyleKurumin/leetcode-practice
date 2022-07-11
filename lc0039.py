# coding=utf-8

from typing import List

# @solution-sync:begin
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        ans = []

        def helper(start, target, path):
            if target == 0:
                ans.append(path)
                return

            for i in range(start, len(candidates)):
                if target - candidates[i] < 0:
                    break

                helper(i, target-candidates[i], path + [candidates[i]])

        helper(0, target, [])
        return ans
# @solution-sync:end


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7

    result = Solution().combinationSum(candidates, target)
    print(result)