class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        return self.binary_guess(x, left, right)

    def binary_guess(self, x, left, right):
        while left <= right:
            mid = left + (right - left) // 2
            if self.validate(x, mid):
                if (mid + 1) * mid > x:
                    return mid
                left = mid + 1
            else:
                right = mid - 1
        return right

    def validate(self, x, mid):
        if mid * mid > x:
            return False
        return True
