# coding=utf-8


# @solution-sync:begin
class Solution:
    def reverse(self, x: int) -> int:
        should_be_reversed = False
        reverse = 0

        if str(x)[0] == "-":
            should_be_reversed = True

        x = abs(x)

        while x:
            rem = x % 10
            x = x // 10
            reverse = reverse * 10 + rem

        if reverse > (2 ** 31) - 1 or reverse < -(2 ** 31):
            reverse = 0

        if should_be_reversed:
            return -(reverse)
        else:
            return reverse


# @solution-sync:end


if __name__ == '__main__':
    x = 123

    result = Solution().reverse(x)
    print(result)