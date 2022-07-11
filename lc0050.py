class Solution:
    def myPow(self, x: float, n: int) -> float:
        rev = True if n < 0 else False
        n = abs(n)

        base = 1
        add = x

        while n > 0:
            if n & 1 == 1:
                base *= add
            add *= add
            n >>= 1
        return base if not rev else 1 / base