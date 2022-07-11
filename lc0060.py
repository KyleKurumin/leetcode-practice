import math


class BinaryIndexedTree:
    def __init__(self, n):
        self.tree = [0] * (n + 1)

    def update(self, pos, val):
        pos = pos + 1
        while pos < len(self.tree):
            self.tree[pos] += val
            pos += self.low_bit(pos)

    def query(self, pos):
        pos = pos + 1
        ans = 0
        while pos > 0:
            ans += self.tree[pos]
            pos -= self.low_bit(pos)
        return ans

    def low_bit(self, x):
        return x & (-x)


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k -= 1
        res = ''
        base = math.factorial(n - 1)
        p = n - 1
        fenwick = BinaryIndexedTree(n)
        while p > 0:
            idx = k // base
            cur = self.find(fenwick, idx, n) + 1
            fenwick.update(cur - 1, 1)

            res += str(cur)
            k %= base
            base //= p
            p -= 1
        last = self.find(fenwick, 0, n) + 1
        res += str(last)
        return res

    def find(self, fenwick, pos, n):
        left = 0
        right = n - 1
        result = left

        while left <= right:
            mid = left + (right - left) // 2

            if mid - fenwick.query(mid) >= pos:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result
    