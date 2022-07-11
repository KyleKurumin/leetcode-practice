class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1

        neg = False
        if dividend < 0:
            dividend = -dividend
            neg = ~neg
        if divisor < 0:
            divisor = -divisor
            neg = ~neg

        left = 0
        right = dividend
        result = left
        while left <= right:
            mid = left + (right - left) // 2
            mul = self.quick_mul(mid, divisor)
            if mul <= dividend:
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        result = -result if neg else result
        if result > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif result < - 2 ** 31:
            return - 2 ** 31
        else:
            return result

    def quick_mul(self, a, b):
        base = 0
        add = a
        while b > 0:
            if b & 1 == 1:
                base += add
            add += add
            b >>= 1
        return base