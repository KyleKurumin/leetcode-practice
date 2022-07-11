# coding=utf-8


# @solution-sync:begin
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left = {
            ']': '[',
            ')': '(',
            '}': '{'
        }

        for i in range(len(s)):
            if s[i] in left.values():
                stack.append(s[i])

            else:
                if not stack:
                    return False

                if stack[-1] == left[s[i]]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
# @solution-sync:end


if __name__ == '__main__':
    s = "()"

    result = Solution().isValid(s)
    print(result)
