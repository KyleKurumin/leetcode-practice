import collections
from itertools import groupby


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, res = 0, 1 << 31
        record = {}
        ans = ''

        counter = collections.Counter(t)

        for right in range(len(s)):
            ch = s[right]
            record[ch] = record.get(ch, 0) + 1
            while self.valid(counter, record):
                if right - left + 1 < res:
                    res = right - left + 1
                    ans = s[left: right + 1]

                removed = s[left]
                record[removed] -= 1
                if record[removed] == 0:
                    record.pop(removed)
                left += 1

        return ans

    def valid(self, t, record):
        for ch, times in t.items():
            if record.get(ch, 0) < times:
                return False

        return True