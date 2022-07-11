# coding=utf-8


# @solution-sync:begin
class Solution:
    def countAndSay(self, n: int) -> str:
        base = '1'

        for i in range(1, n):
            base = self.parse(base)

        return base

    def parse(self, s):
        s = s + '*'
        res = ''
        k = 0
        start = 0
        for idx, ch in enumerate(s):
            if ch == s[start]:
                k += 1
            else:
                res += f'{k}{s[idx - 1]}'
                k = 1
                start = idx
        return res


# @solution-sync:end


if __name__ == '__main__':
    n = 1

    result = Solution().countAndSay(n)
    print(result)
