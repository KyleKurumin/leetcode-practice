# coding=utf-8

from typing import List

# @solution-sync:begin
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # find the start position of longest non-decreasing suffix
        i = len(nums) - 1
        while i >= 0 and nums[i - 1] >= nums[i]:
            i -= 1
        # now i is pointing at the position of the last number of current node (pivot)
        i -= 1

        # if the index of the pivot is smaller than 0, it is the last permutation like [3, 2, 1]
        if i >= 0:
            j = len(nums) - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]

        # sort the following elements in available set.
        # Because they are in decreasing order, two pointers is the most efficient method.
        i = i + 1
        j = len(nums) - 1
        while i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
# @solution-sync:end


if __name__ == '__main__':
    nums = [1, 2, 3]
    Solution().nextPermutation(nums)