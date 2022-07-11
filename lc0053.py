import itertools
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = itertools.accumulate(nums)
        min_val = 0
        res = - 1 << 32
        for val in prefix:
            res = max(res, val - min_val)
            min_val = min(min_val, val)
        return res
