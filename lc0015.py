# coding=utf-8

from typing import List

# @solution-sync:begin
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums = sorted(nums)
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            p = i + 1
            q = len(nums) - 1

            target = -nums[i]

            while p < q:
                if nums[p] + nums[q] == target:
                    ans.append([nums[i], nums[p], nums[q]])
                    p += 1
                    q -= 1
                    while i + 1 < p < q and nums[p] == nums[p - 1]:
                        p += 1
                    while p < q < len(nums) - 1 and nums[q] == nums[q + 1]:
                        q -= 1
                elif nums[p] + nums[q] > target:
                    q -= 1
                    while p < q < len(nums) - 1 and nums[q] == nums[q + 1]:
                        q -= 1
                else:
                    p += 1
                    while i + 1 < p < q and nums[p] == nums[p - 1]:
                        p += 1
        return ans
# @solution-sync:end


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]

    result = Solution().threeSum(nums)
    print(result)