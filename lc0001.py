from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}

        for i in range(len(nums)):
            if target - nums[i] in memo:
                return [memo[target - nums[i]], i]

            memo[nums[i]] = i

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9

    result = Solution().twoSum(nums, target)
    print(result)
