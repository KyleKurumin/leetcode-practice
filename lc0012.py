# coding=utf-8


# @solution-sync:begin
class Solution:
    def intToRoman(self, num: int) -> str:
        res = ''

        base = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        ref = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

        for b, r in zip(base, ref):
            if count := (num // b):
                res += r * count
                num %= b

        return res


# @solution-sync:end


if __name__ == '__main__':
    num = 3

    result = Solution().intToRoman(num)
    print(result)