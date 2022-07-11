# coding=utf-8


# @solution-sync:begin
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        mod = 0
        while x > mod:
            mod = x % 10 + mod * 10
            x //= 10

        return mod == x or mod // 10 == x


# @solution-sync:end


if __name__ == '__main__':
    x = 121

    result = Solution().isPalindrome(x)
    print(result)