# coding=utf-8

from typing import List

# @solution-sync:begin
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        total = len(nums1) + len(nums2)
        flg = total & 1
        lb = 0
        ub = len(nums1)

        median1, median2 = 0, 0

        while lb <= ub:
            x = lb + (ub - lb) // 2
            y = (total + 1) // 2 - x

            x_left = -1 << 31 if x == 0 else nums1[x - 1]
            x_right = 1 << 31 if x == len(nums1) else nums1[x]

            y_left = -1 << 31 if y == 0 else nums2[y - 1]
            y_right = 1 << 31 if y == len(nums2) else nums2[y]

            if y_left <= x_right:
                median1, median2 = max(x_left, y_left), min(x_right, y_right)
                ub = x - 1
            else:
                lb = x + 1

        return (median1 + median2) / 2 if not flg else median1
# @solution-sync:end


if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]

    result = Solution().findMedianSortedArrays(nums1, nums2)
    print(result)