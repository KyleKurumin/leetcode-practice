# coding=utf-8


# @solution-sync:begin
class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        ans = []

        for i in range(len(s)):
            cur = symbol[s[i]]
            if i > 0:
                if ans and cur > ans[-1]:
                    ans.append(cur - ans.pop())
                    continue
            ans.append(cur)
        return sum(ans)


# @solution-sync:end


if __name__ == '__main__':
    s = "III"

    result = Solution().romanToInt(s)
    print(result)